# Generated from Regex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser

# This class defines a complete listener for a parse tree produced by RegexParser.
class RegexListener(ParseTreeListener):

    # Enter a parse tree produced by RegexParser#regex.
    def enterRegex(self, ctx:RegexParser.RegexContext):
        pass

    # Exit a parse tree produced by RegexParser#regex.
    def exitRegex(self, ctx:RegexParser.RegexContext):
        pass


    # Enter a parse tree produced by RegexParser#unionExpr.
    def enterUnionExpr(self, ctx:RegexParser.UnionExprContext):
        pass

    # Exit a parse tree produced by RegexParser#unionExpr.
    def exitUnionExpr(self, ctx:RegexParser.UnionExprContext):
        pass


    # Enter a parse tree produced by RegexParser#concatExpr.
    def enterConcatExpr(self, ctx:RegexParser.ConcatExprContext):
        pass

    # Exit a parse tree produced by RegexParser#concatExpr.
    def exitConcatExpr(self, ctx:RegexParser.ConcatExprContext):
        pass


    # Enter a parse tree produced by RegexParser#repeatExpr.
    def enterRepeatExpr(self, ctx:RegexParser.RepeatExprContext):
        pass

    # Exit a parse tree produced by RegexParser#repeatExpr.
    def exitRepeatExpr(self, ctx:RegexParser.RepeatExprContext):
        pass


    # Enter a parse tree produced by RegexParser#postfix.
    def enterPostfix(self, ctx:RegexParser.PostfixContext):
        pass

    # Exit a parse tree produced by RegexParser#postfix.
    def exitPostfix(self, ctx:RegexParser.PostfixContext):
        pass


    # Enter a parse tree produced by RegexParser#atom.
    def enterAtom(self, ctx:RegexParser.AtomContext):
        pass

    # Exit a parse tree produced by RegexParser#atom.
    def exitAtom(self, ctx:RegexParser.AtomContext):
        pass



del RegexParser