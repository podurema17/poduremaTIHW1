from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Sequence, Set, Tuple

from antlr4 import BailErrorStrategy, CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

from regex_grammar.RegexLexer import RegexLexer
from regex_grammar.RegexParser import RegexParser
from regex_grammar.RegexVisitor import RegexVisitor


class _RegexSyntaxError(ValueError):
    """Custom error to differentiate syntax issues."""


class _RaisingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise _RegexSyntaxError(f"Invalid regex near column {column}: {msg}")


class State:
    __slots__ = ("id", "transitions", "epsilons")

    def __init__(self, state_id: int):
        self.id = state_id
        self.transitions: dict[int, List[State]] = {}
        self.epsilons: List[State] = []

    def add_transition(self, symbol: int, target: "State") -> None:
        self.transitions.setdefault(symbol, []).append(target)

    def add_epsilon(self, target: "State") -> None:
        self.epsilons.append(target)


@dataclass
class _Fragment:
    start: State
    accepts: Sequence[State]


class _ThompsonVisitor(RegexVisitor):
    def __init__(self) -> None:
        super().__init__()
        self._states: List[State] = []
        self._next_id = 0

    def build(self, tree) -> "RegexNFA":
        fragment = self.visit(tree)
        if not fragment.accepts:
            raise ValueError("Regex must have at least one accept state")
        if len(fragment.accepts) != 1:
            raise ValueError("Fragment expected to have exactly one accept state")
        accept = fragment.accepts[0]
        return RegexNFA(fragment.start, accept, tuple(self._states))

    def _state(self) -> State:
        st = State(self._next_id)
        self._next_id += 1
        self._states.append(st)
        return st

    def visitRegex(self, ctx: RegexParser.RegexContext):
        return self.visit(ctx.unionExpr())

    def visitUnionExpr(self, ctx: RegexParser.UnionExprContext):
        fragments = [self.visit(child) for child in ctx.concatExpr()]
        if len(fragments) == 1:
            return fragments[0]
        start = self._state()
        end = self._state()
        for fragment in fragments:
            start.add_epsilon(fragment.start)
            for accept in fragment.accepts:
                accept.add_epsilon(end)
        return _Fragment(start, (end,))

    def visitConcatExpr(self, ctx: RegexParser.ConcatExprContext):
        fragments = [self.visit(child) for child in ctx.repeatExpr()]
        current = fragments[0]
        for fragment in fragments[1:]:
            for accept in current.accepts:
                accept.add_epsilon(fragment.start)
            current = _Fragment(current.start, fragment.accepts)
        return current

    def visitRepeatExpr(self, ctx: RegexParser.RepeatExprContext):
        fragment = self.visit(ctx.atom())
        postfix = ctx.postfix()
        if postfix is None:
            return fragment
        op = postfix.getText()
        if op == "*":
            return self._apply_star(fragment)
        if op == "+":
            return self._apply_plus(fragment)
        if op == "?":
            return self._apply_question(fragment)
        raise ValueError(f"Unsupported postfix operator {op}")

    def visitAtom(self, ctx: RegexParser.AtomContext):
        if ctx.DIGIT():
            sym = int(ctx.DIGIT().getText())
            start = self._state()
            end = self._state()
            start.add_transition(sym, end)
            return _Fragment(start, (end,))
        inner = self.visit(ctx.unionExpr())
        return inner

    def _apply_star(self, fragment: _Fragment) -> _Fragment:
        start = self._state()
        end = self._state()
        start.add_epsilon(fragment.start)
        start.add_epsilon(end)
        for accept in fragment.accepts:
            accept.add_epsilon(fragment.start)
            accept.add_epsilon(end)
        return _Fragment(start, (end,))

    def _apply_plus(self, fragment: _Fragment) -> _Fragment:
        start = self._state()
        end = self._state()
        start.add_epsilon(fragment.start)
        for accept in fragment.accepts:
            accept.add_epsilon(fragment.start)
            accept.add_epsilon(end)
        return _Fragment(start, (end,))

    def _apply_question(self, fragment: _Fragment) -> _Fragment:
        start = self._state()
        end = self._state()
        start.add_epsilon(fragment.start)
        start.add_epsilon(end)
        for accept in fragment.accepts:
            accept.add_epsilon(end)
        return _Fragment(start, (end,))


class RegexNFA:
    def __init__(self, start: State, accept: State, states: Tuple[State, ...]):
        self.start = start
        self.accept = accept
        self.states = states

    def matches(self, input_str: str) -> bool:
        current = self._epsilon_closure({self.start})
        for ch in input_str:
            if ch < "0" or ch > "9":
                raise ValueError("Input must only contain digits 0-9")
            sym = ord(ch) - ord("0")
            next_states: Set[State] = set()
            for st in current:
                for target in st.transitions.get(sym, ()):
                    next_states.update(self._epsilon_closure({target}))
            current = next_states
            if not current:
                return False
        return self.accept in current

    @staticmethod
    def _epsilon_closure(states: Iterable[State]) -> Set[State]:
        stack = list(states)
        closure = set(stack)
        while stack:
            st = stack.pop()
            for nxt in st.epsilons:
                if nxt not in closure:
                    closure.add(nxt)
                    stack.append(nxt)
        return closure


def _parse_regex(regex: str) -> RegexParser.RegexContext:
    if not isinstance(regex, str):
        raise TypeError("Regex must be a string")
    input_stream = InputStream(regex)
    lexer = RegexLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(_RaisingErrorListener())
    token_stream = CommonTokenStream(lexer)
    parser = RegexParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(_RaisingErrorListener())
    parser._errHandler = BailErrorStrategy()
    try:
        return parser.regex()
    except ParseCancellationException as exc:
        raise _RegexSyntaxError("Invalid regular expression") from exc


def build_nfa_from_regex(regex: str) -> RegexNFA:
    tree = _parse_regex(regex)
    visitor = _ThompsonVisitor()
    return visitor.build(tree)


def task3(args: Sequence[str]) -> bool:
    if len(args) != 2:
        raise ValueError("Usage: task3(<regex>, <input_string>)")
    regex, input_value = args
    nfa = build_nfa_from_regex(regex)
    return nfa.matches(input_value)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python task3.py <regex> <input_string>")
        sys.exit(1)
    try:
        accepted = task3(sys.argv[1:])
    except Exception as exc:  # pragma: no cover - CLI feedback
        print(f"Error: {exc}")
        sys.exit(2)
    print("ACCEPTED" if accepted else "REJECTED")

