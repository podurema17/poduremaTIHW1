# Generated from Regex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser

# This class defines a complete generic visitor for a parse tree produced by RegexParser.

class RegexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegexParser#regex.
    def visitRegex(self, ctx:RegexParser.RegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#unionExpr.
    def visitUnionExpr(self, ctx:RegexParser.UnionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#concatExpr.
    def visitConcatExpr(self, ctx:RegexParser.ConcatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#repeatExpr.
    def visitRepeatExpr(self, ctx:RegexParser.RepeatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#postfix.
    def visitPostfix(self, ctx:RegexParser.PostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#atom.
    def visitAtom(self, ctx:RegexParser.AtomContext):
        return self.visitChildren(ctx)



del RegexParser