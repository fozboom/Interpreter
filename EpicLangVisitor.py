# Generated from EpicLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EpicLangParser import EpicLangParser
else:
    from EpicLangParser import EpicLangParser

# This class defines a complete generic visitor for a parse tree produced by EpicLangParser.

class EpicLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EpicLangParser#program.
    def visitProgram(self, ctx:EpicLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#funcDef.
    def visitFuncDef(self, ctx:EpicLangParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#params.
    def visitParams(self, ctx:EpicLangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#block.
    def visitBlock(self, ctx:EpicLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#statement.
    def visitStatement(self, ctx:EpicLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#break.
    def visitBreak(self, ctx:EpicLangParser.BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#continue.
    def visitContinue(self, ctx:EpicLangParser.ContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#ListLiteralIndexExpr.
    def visitListLiteralIndexExpr(self, ctx:EpicLangParser.ListLiteralIndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#UnaryExpr.
    def visitUnaryExpr(self, ctx:EpicLangParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#FunctionCallExpr.
    def visitFunctionCallExpr(self, ctx:EpicLangParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:EpicLangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#EqualityExpr.
    def visitEqualityExpr(self, ctx:EpicLangParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#ListLiteralExpr.
    def visitListLiteralExpr(self, ctx:EpicLangParser.ListLiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#CompareExpr.
    def visitCompareExpr(self, ctx:EpicLangParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#ListIndexExpr.
    def visitListIndexExpr(self, ctx:EpicLangParser.ListIndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:EpicLangParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#VarExpr.
    def visitVarExpr(self, ctx:EpicLangParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#ParenExpr.
    def visitParenExpr(self, ctx:EpicLangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:EpicLangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#LogicalExpr.
    def visitLogicalExpr(self, ctx:EpicLangParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#ExpressionListIndexExpr.
    def visitExpressionListIndexExpr(self, ctx:EpicLangParser.ExpressionListIndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#indexSequence.
    def visitIndexSequence(self, ctx:EpicLangParser.IndexSequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#functionCall.
    def visitFunctionCall(self, ctx:EpicLangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#argumentList.
    def visitArgumentList(self, ctx:EpicLangParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#SimpleAssignment.
    def visitSimpleAssignment(self, ctx:EpicLangParser.SimpleAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#ListIndexAssignment.
    def visitListIndexAssignment(self, ctx:EpicLangParser.ListIndexAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#ifStatement.
    def visitIfStatement(self, ctx:EpicLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#whileStatement.
    def visitWhileStatement(self, ctx:EpicLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#forStatement.
    def visitForStatement(self, ctx:EpicLangParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#returnStatement.
    def visitReturnStatement(self, ctx:EpicLangParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#printStatement.
    def visitPrintStatement(self, ctx:EpicLangParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#literal.
    def visitLiteral(self, ctx:EpicLangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EpicLangParser#listLiteral.
    def visitListLiteral(self, ctx:EpicLangParser.ListLiteralContext):
        return self.visitChildren(ctx)



del EpicLangParser