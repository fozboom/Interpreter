# Generated from EpicLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EpicLangParser import EpicLangParser
else:
    from EpicLangParser import EpicLangParser

# This class defines a complete listener for a parse tree produced by EpicLangParser.
class EpicLangListener(ParseTreeListener):

    # Enter a parse tree produced by EpicLangParser#program.
    def enterProgram(self, ctx:EpicLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by EpicLangParser#program.
    def exitProgram(self, ctx:EpicLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by EpicLangParser#funcDef.
    def enterFuncDef(self, ctx:EpicLangParser.FuncDefContext):
        pass

    # Exit a parse tree produced by EpicLangParser#funcDef.
    def exitFuncDef(self, ctx:EpicLangParser.FuncDefContext):
        pass


    # Enter a parse tree produced by EpicLangParser#params.
    def enterParams(self, ctx:EpicLangParser.ParamsContext):
        pass

    # Exit a parse tree produced by EpicLangParser#params.
    def exitParams(self, ctx:EpicLangParser.ParamsContext):
        pass


    # Enter a parse tree produced by EpicLangParser#block.
    def enterBlock(self, ctx:EpicLangParser.BlockContext):
        pass

    # Exit a parse tree produced by EpicLangParser#block.
    def exitBlock(self, ctx:EpicLangParser.BlockContext):
        pass


    # Enter a parse tree produced by EpicLangParser#statement.
    def enterStatement(self, ctx:EpicLangParser.StatementContext):
        pass

    # Exit a parse tree produced by EpicLangParser#statement.
    def exitStatement(self, ctx:EpicLangParser.StatementContext):
        pass


    # Enter a parse tree produced by EpicLangParser#break.
    def enterBreak(self, ctx:EpicLangParser.BreakContext):
        pass

    # Exit a parse tree produced by EpicLangParser#break.
    def exitBreak(self, ctx:EpicLangParser.BreakContext):
        pass


    # Enter a parse tree produced by EpicLangParser#continue.
    def enterContinue(self, ctx:EpicLangParser.ContinueContext):
        pass

    # Exit a parse tree produced by EpicLangParser#continue.
    def exitContinue(self, ctx:EpicLangParser.ContinueContext):
        pass


    # Enter a parse tree produced by EpicLangParser#ListLiteralIndexExpr.
    def enterListLiteralIndexExpr(self, ctx:EpicLangParser.ListLiteralIndexExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#ListLiteralIndexExpr.
    def exitListLiteralIndexExpr(self, ctx:EpicLangParser.ListLiteralIndexExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#UnaryExpr.
    def enterUnaryExpr(self, ctx:EpicLangParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#UnaryExpr.
    def exitUnaryExpr(self, ctx:EpicLangParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#FunctionCallExpr.
    def enterFunctionCallExpr(self, ctx:EpicLangParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#FunctionCallExpr.
    def exitFunctionCallExpr(self, ctx:EpicLangParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:EpicLangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:EpicLangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#EqualityExpr.
    def enterEqualityExpr(self, ctx:EpicLangParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#EqualityExpr.
    def exitEqualityExpr(self, ctx:EpicLangParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#ListLiteralExpr.
    def enterListLiteralExpr(self, ctx:EpicLangParser.ListLiteralExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#ListLiteralExpr.
    def exitListLiteralExpr(self, ctx:EpicLangParser.ListLiteralExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#CompareExpr.
    def enterCompareExpr(self, ctx:EpicLangParser.CompareExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#CompareExpr.
    def exitCompareExpr(self, ctx:EpicLangParser.CompareExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#ListIndexExpr.
    def enterListIndexExpr(self, ctx:EpicLangParser.ListIndexExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#ListIndexExpr.
    def exitListIndexExpr(self, ctx:EpicLangParser.ListIndexExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:EpicLangParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:EpicLangParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#VarExpr.
    def enterVarExpr(self, ctx:EpicLangParser.VarExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#VarExpr.
    def exitVarExpr(self, ctx:EpicLangParser.VarExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#ParenExpr.
    def enterParenExpr(self, ctx:EpicLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#ParenExpr.
    def exitParenExpr(self, ctx:EpicLangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:EpicLangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:EpicLangParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#LogicalExpr.
    def enterLogicalExpr(self, ctx:EpicLangParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#LogicalExpr.
    def exitLogicalExpr(self, ctx:EpicLangParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#ExpressionListIndexExpr.
    def enterExpressionListIndexExpr(self, ctx:EpicLangParser.ExpressionListIndexExprContext):
        pass

    # Exit a parse tree produced by EpicLangParser#ExpressionListIndexExpr.
    def exitExpressionListIndexExpr(self, ctx:EpicLangParser.ExpressionListIndexExprContext):
        pass


    # Enter a parse tree produced by EpicLangParser#indexSequence.
    def enterIndexSequence(self, ctx:EpicLangParser.IndexSequenceContext):
        pass

    # Exit a parse tree produced by EpicLangParser#indexSequence.
    def exitIndexSequence(self, ctx:EpicLangParser.IndexSequenceContext):
        pass


    # Enter a parse tree produced by EpicLangParser#functionCall.
    def enterFunctionCall(self, ctx:EpicLangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by EpicLangParser#functionCall.
    def exitFunctionCall(self, ctx:EpicLangParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by EpicLangParser#argumentList.
    def enterArgumentList(self, ctx:EpicLangParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by EpicLangParser#argumentList.
    def exitArgumentList(self, ctx:EpicLangParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by EpicLangParser#SimpleAssignment.
    def enterSimpleAssignment(self, ctx:EpicLangParser.SimpleAssignmentContext):
        pass

    # Exit a parse tree produced by EpicLangParser#SimpleAssignment.
    def exitSimpleAssignment(self, ctx:EpicLangParser.SimpleAssignmentContext):
        pass


    # Enter a parse tree produced by EpicLangParser#ListIndexAssignment.
    def enterListIndexAssignment(self, ctx:EpicLangParser.ListIndexAssignmentContext):
        pass

    # Exit a parse tree produced by EpicLangParser#ListIndexAssignment.
    def exitListIndexAssignment(self, ctx:EpicLangParser.ListIndexAssignmentContext):
        pass


    # Enter a parse tree produced by EpicLangParser#ifStatement.
    def enterIfStatement(self, ctx:EpicLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by EpicLangParser#ifStatement.
    def exitIfStatement(self, ctx:EpicLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by EpicLangParser#whileStatement.
    def enterWhileStatement(self, ctx:EpicLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by EpicLangParser#whileStatement.
    def exitWhileStatement(self, ctx:EpicLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by EpicLangParser#forStatement.
    def enterForStatement(self, ctx:EpicLangParser.ForStatementContext):
        pass

    # Exit a parse tree produced by EpicLangParser#forStatement.
    def exitForStatement(self, ctx:EpicLangParser.ForStatementContext):
        pass


    # Enter a parse tree produced by EpicLangParser#returnStatement.
    def enterReturnStatement(self, ctx:EpicLangParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by EpicLangParser#returnStatement.
    def exitReturnStatement(self, ctx:EpicLangParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by EpicLangParser#printStatement.
    def enterPrintStatement(self, ctx:EpicLangParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by EpicLangParser#printStatement.
    def exitPrintStatement(self, ctx:EpicLangParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by EpicLangParser#literal.
    def enterLiteral(self, ctx:EpicLangParser.LiteralContext):
        pass

    # Exit a parse tree produced by EpicLangParser#literal.
    def exitLiteral(self, ctx:EpicLangParser.LiteralContext):
        pass


    # Enter a parse tree produced by EpicLangParser#listLiteral.
    def enterListLiteral(self, ctx:EpicLangParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by EpicLangParser#listLiteral.
    def exitListLiteral(self, ctx:EpicLangParser.ListLiteralContext):
        pass



del EpicLangParser