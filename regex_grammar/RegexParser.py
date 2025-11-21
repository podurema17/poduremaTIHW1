# Generated from Regex.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,42,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,0,
        1,0,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,2,4,2,25,8,2,11,2,
        12,2,26,1,3,1,3,3,3,31,8,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,40,8,
        5,1,5,0,0,6,0,2,4,6,8,10,0,1,1,0,2,4,39,0,12,1,0,0,0,2,15,1,0,0,
        0,4,24,1,0,0,0,6,28,1,0,0,0,8,32,1,0,0,0,10,39,1,0,0,0,12,13,3,2,
        1,0,13,14,5,0,0,1,14,1,1,0,0,0,15,20,3,4,2,0,16,17,5,1,0,0,17,19,
        3,4,2,0,18,16,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,
        21,3,1,0,0,0,22,20,1,0,0,0,23,25,3,6,3,0,24,23,1,0,0,0,25,26,1,0,
        0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,5,1,0,0,0,28,30,3,10,5,0,29,31,
        3,8,4,0,30,29,1,0,0,0,30,31,1,0,0,0,31,7,1,0,0,0,32,33,7,0,0,0,33,
        9,1,0,0,0,34,40,5,7,0,0,35,36,5,5,0,0,36,37,3,2,1,0,37,38,5,6,0,
        0,38,40,1,0,0,0,39,34,1,0,0,0,39,35,1,0,0,0,40,11,1,0,0,0,4,20,26,
        30,39
    ]

class RegexParser ( Parser ):

    grammarFileName = "Regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'*'", "'+'", "'?'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "DIGIT", "WS" ]

    RULE_regex = 0
    RULE_unionExpr = 1
    RULE_concatExpr = 2
    RULE_repeatExpr = 3
    RULE_postfix = 4
    RULE_atom = 5

    ruleNames =  [ "regex", "unionExpr", "concatExpr", "repeatExpr", "postfix", 
                   "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    DIGIT=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RegexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unionExpr(self):
            return self.getTypedRuleContext(RegexParser.UnionExprContext,0)


        def EOF(self):
            return self.getToken(RegexParser.EOF, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_regex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegex" ):
                listener.enterRegex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegex" ):
                listener.exitRegex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegex" ):
                return visitor.visitRegex(self)
            else:
                return visitor.visitChildren(self)




    def regex(self):

        localctx = RegexParser.RegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_regex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.unionExpr()
            self.state = 13
            self.match(RegexParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concatExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegexParser.ConcatExprContext)
            else:
                return self.getTypedRuleContext(RegexParser.ConcatExprContext,i)


        def getRuleIndex(self):
            return RegexParser.RULE_unionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnionExpr" ):
                listener.enterUnionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnionExpr" ):
                listener.exitUnionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnionExpr" ):
                return visitor.visitUnionExpr(self)
            else:
                return visitor.visitChildren(self)




    def unionExpr(self):

        localctx = RegexParser.UnionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_unionExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.concatExpr()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 16
                self.match(RegexParser.T__0)
                self.state = 17
                self.concatExpr()
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcatExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def repeatExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegexParser.RepeatExprContext)
            else:
                return self.getTypedRuleContext(RegexParser.RepeatExprContext,i)


        def getRuleIndex(self):
            return RegexParser.RULE_concatExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatExpr" ):
                listener.enterConcatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatExpr" ):
                listener.exitConcatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatExpr" ):
                return visitor.visitConcatExpr(self)
            else:
                return visitor.visitChildren(self)




    def concatExpr(self):

        localctx = RegexParser.ConcatExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_concatExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 23
                self.repeatExpr()
                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(RegexParser.AtomContext,0)


        def postfix(self):
            return self.getTypedRuleContext(RegexParser.PostfixContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_repeatExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeatExpr" ):
                listener.enterRepeatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeatExpr" ):
                listener.exitRepeatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeatExpr" ):
                return visitor.visitRepeatExpr(self)
            else:
                return visitor.visitChildren(self)




    def repeatExpr(self):

        localctx = RegexParser.RepeatExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_repeatExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.atom()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                self.state = 29
                self.postfix()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegexParser.RULE_postfix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix" ):
                listener.enterPostfix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix" ):
                listener.exitPostfix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix" ):
                return visitor.visitPostfix(self)
            else:
                return visitor.visitChildren(self)




    def postfix(self):

        localctx = RegexParser.PostfixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_postfix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(RegexParser.DIGIT, 0)

        def unionExpr(self):
            return self.getTypedRuleContext(RegexParser.UnionExprContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = RegexParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(RegexParser.DIGIT)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(RegexParser.T__4)
                self.state = 36
                self.unionExpr()
                self.state = 37
                self.match(RegexParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





