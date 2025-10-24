from collections import deque, defaultdict

class DFA:
    def __init__(self, states, alphabet, start, accepts, trans):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.start = start
        self.accepts = set(accepts)
        self.trans = {q: dict(trans.get(q, {})) for q in self.states}
        need_sink = any(a not in self.trans.get(q, {}) for q in self.states for a in self.alphabet)
        if need_sink:
            sink = "__SINK__"
            while sink in self.states:
                sink += "_"
            self.states.add(sink)
            self.trans.setdefault(sink, {})
            for a in self.alphabet:
                self.trans[sink][a] = sink
            for q in list(self.states):
                self.trans.setdefault(q, {})
                for a in self.alphabet:
                    self.trans[q].setdefault(a, sink)
        else:
            for q in self.states:
                self.trans.setdefault(q, {})
                for a in self.alphabet:
                    self.trans[q].setdefault(a, q)

    def reachable(self):
        vis = set()
        dq = deque([self.start])
        while dq:
            q = dq.popleft()
            if q in vis:
                continue
            vis.add(q)
            for a in self.alphabet:
                dq.append(self.trans[q][a])
        return vis

def minimize_dfa(dfa):
    Q = dfa.reachable()
    Σ = dfa.alphabet
    F = dfa.accepts & Q
    NF = Q - F
    P = [F, NF] if F and NF else [Q]
    inv = {a: defaultdict(set) for a in Σ}
    for q in Q:
        for a in Σ:
            inv[a][dfa.trans[q][a]].add(q)
    W = deque([F, NF] if F and NF else [Q])
    while W:
        A = W.popleft()
        for a in Σ:
            X = set()
            for r in A:
                X |= inv[a][r]
            if not X:
                continue
            newP = []
            for Y in P:
                i = Y & X
                d = Y - X
                if i and d:
                    newP.extend([i, d])
                    if Y in W:
                        W.remove(Y)
                        W.append(i)
                        W.append(d)
                    else:
                        W.append(i if len(i) <= len(d) else d)
                else:
                    newP.append(Y)
            P = newP
    rep = {}
    for block in P:
        r = next(iter(block))
        for q in block:
            rep[q] = r
    new_states = {rep[q] for q in Q}
    new_start = rep[dfa.start]
    new_accepts = {rep[q] for q in F}
    new_trans = {r: {} for r in new_states}
    for q in Q:
        r = rep[q]
        for a in Σ:
            new_trans[r][a] = rep[dfa.trans[q][a]]
    return DFA(new_states, Σ, new_start, new_accepts, new_trans)

def equivalent_dfa(d1, d2):
    Σ = d1.alphabet | d2.alphabet
    d1 = DFA(d1.states, Σ, d1.start, d1.accepts, d1.trans)
    d2 = DFA(d2.states, Σ, d2.start, d2.accepts, d2.trans)
    start = (d1.start, d2.start)
    vis = {start}
    dq = deque([start])
    while dq:
        p, q = dq.popleft()
        if (p in d1.accepts) ^ (q in d2.accepts):
            return False
        for a in Σ:
            np = d1.trans[p][a]
            nq = d2.trans[q][a]
            pair = (np, nq)
            if pair not in vis:
                vis.add(pair)
                dq.append(pair)
    return True

def is_universal(dfa):
    R = dfa.reachable()
    return bool(R) and R.issubset(dfa.accepts)
