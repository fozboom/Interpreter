import sys

from antlr4 import CommonTokenStream, FileStream
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener

from EpicLangLexer import EpicLangLexer
from EpicLangParser import EpicLangParser
from EpicLangVisitor import EpicLangVisitor


class ErrorHandler(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("syntax error")
        sys.exit(0)


class EpicLang(EpicLangVisitor):
    def __init__(self):
        super().__init__()
        self.functions = dict()
        self.variables = {}
        self.loop_depth = 0
        self.return_value = None

    def visitProgram(self, ctx: EpicLangParser.ProgramContext):
        for func in ctx.funcDef():
            self.visit(func)

        if "main" not in self.functions:
            print("runtime error")
            sys.exit(0)
        main_func = self.functions["main"]
        if len(main_func["params"]) > 0:
            print("runtime error")
            sys.exit(0)

        self.visitBlock(main_func["block"])

    def visitFuncDef(self, ctx: EpicLangParser.FuncDefContext):
        func_name = ctx.IDENTIFIER().getText()
        params = (
            [param.getText() for param in ctx.params().IDENTIFIER()]
            if ctx.params()
            else []
        )
        if func_name in self.functions:
            print("runtime error")
            sys.exit(0)
        self.functions[func_name] = {"params": params, "block": ctx.block()}

    def _processFunctionCall(self, func_name, args):
        if func_name == "len":
            if len(args) == 0:
                return 0
            elif not isinstance(args[0], list):
                print("runtime error")
                sys.exit(0)
            return len(args[0])

        if func_name not in self.functions:
            print("runtime error")
            sys.exit(0)

        func = self.functions[func_name]
        expected_params = func["params"]

        if len(args) != len(expected_params):
            print("runtime error")
            sys.exit(0)

        old_variables = self.variables.copy()

        self.variables = dict(zip(expected_params, args))

        self.return_value = None
        self.visit(func["block"])

        self.variables = old_variables

        return self.return_value

    def visitFunctionCallExpr(self, ctx: EpicLangParser.FunctionCallExprContext):
        # Определяем имя функции
        if ctx.functionCall().LEN():
            func_name = "len"
        elif ctx.functionCall().IDENTIFIER():
            func_name = ctx.functionCall().IDENTIFIER().getText()
        else:
            print("runtime error")
            sys.exit(0)

        # Обрабатываем аргументы функции
        if ctx.functionCall().argumentList():
            # Если у функции есть список аргументов
            args = [
                self.visit(arg)
                for arg in ctx.functionCall().argumentList().expression()
            ]
        elif ctx.functionCall().expression():
            # Если аргументом является выражение (например, listLiteral)
            args = [self.visit(ctx.functionCall().expression())]
        else:
            # Если аргументов вообще нет
            args = []

        return self._processFunctionCall(func_name, args)

    def visitBlock(self, ctx: EpicLangParser.BlockContext):
        for statement in ctx.statement():
            self.visit(statement)

    def visitWhileStatement(self, ctx: EpicLangParser.WhileStatementContext):
        self.loop_depth += 1
        while True:
            condition = self.visit(ctx.expression())

            if not isinstance(condition, bool):
                print("runtime error")
                sys.exit(0)

            if not condition:
                break

            self.visit(ctx.statement())

        self.loop_depth -= 1

    def visitFunctionCall(self, ctx: EpicLangParser.FunctionCallContext):
        func_name = ctx.IDENTIFIER().getText()
        args = (
            [self.visit(arg) for arg in ctx.argumentList().expression()]
            if ctx.argumentList()
            else []
        )
        return self._processFunctionCall(func_name, args)

    def visitBreak(self, ctx: EpicLangParser.BreakContext):
        if self.loop_depth == 0:
            print("runtime error")
            sys.exit(0)

    def visitContinue(self, ctx: EpicLangParser.ContinueContext):
        if self.loop_depth == 0:
            print("runtime error")
            sys.exit(0)

    def visitIfStatement(self, ctx: EpicLangParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        if not isinstance(condition, bool):
            print("runtime error")
            sys.exit(0)
        if condition:  # if the condition is true
            self.visit(ctx.statement(0))
        elif ctx.statement(1):  # if there is an else statement
            self.visit(ctx.statement(1))

    def visitLiteralExpr(self, ctx: EpicLangParser.LiteralExprContext):
        literal_ctx = ctx.literal()
        if literal_ctx.INT():
            return int(literal_ctx.INT().getText())
        elif literal_ctx.getText() == "true":
            return True
        elif literal_ctx.getText() == "false":
            return False
        elif literal_ctx.getText() == "none":
            return None
        elif literal_ctx.listLiteral():
            return self.visit(literal_ctx.listLiteral())

    def visitForStatement(self, ctx: EpicLangParser.ForStatementContext):
        var_name = ctx.IDENTIFIER().getText()
        start = self.visit(ctx.expression(0))
        end = self.visit(ctx.expression(1))

        if not isinstance(start, int) or not isinstance(end, int):
            print("runtime error")
            sys.exit(0)

        old_value = self.variables.get(var_name, None)
        self.loop_depth += 1
        try:
            for i in range(start, end):
                self.variables[var_name] = i
                self.visit(ctx.statement())
        finally:
            if old_value is None:
                del self.variables[var_name]
            else:
                self.variables[var_name] = old_value
            self.loop_depth -= 1

    def visitExpression(self, ctx: EpicLangParser.ExpressionContext):
        # If this is a function call
        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        # If this is an identifier
        elif ctx.IDENTIFIER() and not ctx.getChildCount() > 1:
            var_name = ctx.IDENTIFIER().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                print("runtime error")
                sys.exit(0)

        # If this is an index access
        elif ctx.getChildCount() == 4 and ctx.getChild(1).getText() == "[":
            var_name = ctx.IDENTIFIER().getText()
            index = self.visit(ctx.expression())
            if var_name not in self.variables:
                print("runtime error")
                sys.exit(0)

            value = self.variables[var_name]

            if not isinstance(value, list):
                print("runtime error")
                sys.exit(0)
            if not isinstance(index, int):
                print("runtime error")
                sys.exit(0)

            if index < 0 or index >= len(value):
                print("runtime error")
                sys.exit(0)

            return value[index]

        # If this is the literal
        elif ctx.literal():
            return self.visit(ctx.literal())

    def visitPrintStatement(self, ctx: EpicLangParser.PrintStatementContext):
        print(self.visit(ctx.expression()))

    def visitReturnStatement(self, ctx: EpicLangParser.ReturnStatementContext):
        if ctx.expression():
            self.return_value = self.visit(ctx.expression())
        else:
            self.return_value = None

    def visitAddSubExpr(self, ctx: EpicLangParser.AddSubExprContext):
        op = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
        }
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.text == "+" and isinstance(left, list) and isinstance(right, list):
            return left + right
        if not isinstance(left, (int, list)) or not isinstance(right, (int, list)):
            print("runtime error")
            sys.exit(0)
        return op[ctx.op.text](left, right)

    def visitMulDivExpr(self, ctx: EpicLangParser.MulDivExprContext):
        op = {
            "*": lambda x, y: x * y,
            "/": lambda x, y: x // y,
            "%": lambda x, y: x % y,
        }

        left = self.visit(ctx.expression(0))

        right = self.visit(ctx.expression(1))
        if ctx.op.text in ["/", "%"] and right == 0:
            print("runtime error")
            sys.exit(0)
        if not isinstance(left, int) or not isinstance(right, int):
            print("runtime error")
            sys.exit(0)
        return op[ctx.op.text](left, right)

    def visitUnaryExprForList(self, item):
        if isinstance(item, list):
            return [self.visitUnaryExprForList(sub_item) for sub_item in item]
        return -item

    def visitUnaryExpr(self, ctx: EpicLangParser.UnaryExprContext):
        op = {
            "-": lambda x: -x,
            "+": lambda x: x,
            "!": lambda x: not x,
        }
        value = self.visit(ctx.expression())

        if isinstance(value, int):
            return op[ctx.op.text](value)
        elif isinstance(value, list):
            if ctx.op.text == "!":
                return not bool(value)
            elif ctx.op.text == "-":
                return [self.visitUnaryExprForList(item) for item in value]
            elif ctx.op.text == "+":
                return value
        elif isinstance(value, bool):
            if ctx.op.text == "!":
                return not value
        else:
            print("runtime error")
            sys.exit(0)

    def visitVarExpr(self, ctx: EpicLangParser.VarExprContext):
        var_name = ctx.IDENTIFIER().getText()
        if var_name in self.variables:
            value = self.variables[var_name]
            return value
        else:
            print("runtime error")
            sys.exit(0)

    def visitListIndexExpr(self, ctx: EpicLangParser.ListIndexExprContext):
        var_name = ctx.IDENTIFIER().getText()

        if var_name not in self.variables:
            print("runtime error")
            sys.exit(0)

        value = self.variables[var_name]
        if not isinstance(value, list):
            print("runtime error")
            sys.exit(0)

        indices = ctx.indexSequence().expression()
        for index_expr in indices:
            index = self.visit(index_expr)

            # Проверяем, что индекс — это целое число
            if not isinstance(index, int):
                print("runtime error")
                sys.exit(0)

            # Проверяем границы списка
            if index < 0 or index >= len(value):
                print("runtime error")
                sys.exit(0)

            # Делаем шаг к следующему элементу
            value = value[index]

        return value

    def visitListLiteral(self, ctx: EpicLangParser.ListLiteralContext):
        return (
            [self.visit(expr) for expr in ctx.expression()] if ctx.expression() else []
        )

    def visitListLiteralExpr(self, ctx: EpicLangParser.ListLiteralExprContext):
        return (
            [self.visit(expr) for expr in ctx.expression()] if ctx.expression() else []
        )

    def visitSimpleAssignment(self, ctx: EpicLangParser.SimpleAssignmentContext):
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value

    def visitListIndexAssignment(self, ctx: EpicLangParser.ListIndexAssignmentContext):
        var_name = ctx.IDENTIFIER().getText()
        index = self.visit(ctx.expression(0))
        value = self.visit(ctx.expression(1))

        if var_name not in self.variables:
            print("runtime error")
            sys.exit(0)

        lst = self.variables[var_name]
        if not isinstance(lst, list):
            print("runtime error")
            sys.exit(0)

        if not isinstance(index, int):
            print("runtime error")
            sys.exit(0)

        if index < 0 or index >= len(lst):
            print("runtime error")
            sys.exit(0)

        lst[index] = value

    def visitParenExpr(self, ctx: EpicLangParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitCompareExpr(self, ctx: EpicLangParser.CompareExprContext):
        op = {
            "<": lambda x, y: x < y,
            "<=": lambda x, y: x <= y,
            ">": lambda x, y: x > y,
            ">=": lambda x, y: x >= y,
        }
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            print("runtime error")
            sys.exit(0)
        return op[ctx.op.text](left, right)

    # def visitAndExpr(self, ctx: EpicLangParser.AndExprContext):
    #     left = self.visit(ctx.expression(0))
    #     right = self.visit(ctx.expression(1))
    #     if not isinstance(left, bool) or not isinstance(right, bool):
    #         print("runtime error")
    #         sys.exit(0)
    #     return left and right

    # def visitOrExpr(self, ctx: EpicLangParser.OrExprContext):
    #     left = self.visit(ctx.expression(0))
    #     right = self.visit(ctx.expression(1))

    #     if not isinstance(left, bool) or not isinstance(right, bool):
    #         print("runtime error")
    #         sys.exit(0)

    #     return left or right

    def visitLogicalExpr(self, ctx: EpicLangParser.LogicalExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if not isinstance(left, bool) or not isinstance(right, bool):
            print("runtime error")
            sys.exit(0)
        if ctx.op.text == "|":
            return left or right
        else:
            return left and right

    def visitEqualityExpr(self, ctx: EpicLangParser.EqualityExprContext):
        expressions = ctx.expression()

        # Получаем первое значение
        left = self.visit(expressions[0])

        # Для каждого следующего выражения проверяем равенство с предыдущим
        for i in range(1, len(expressions)):
            right = self.visit(expressions[i])
            if ctx.op.text == "==":
                if left != right:  # Если хоть одно сравнение ложно
                    return False
            else:  # для !=
                if left == right:  # Если хоть одно сравнение истинно
                    return False
            left = right  # Обновляем левый операнд для следующего сравнения

        return True

    def visitListLiteralIndexExpr(
        self, ctx: EpicLangParser.ListLiteralIndexExprContext
    ):
        list_value = self.visit(ctx.listLiteral())

        if not isinstance(list_value, list):
            print("runtime error")
            sys.exit(0)

        index = self.visit(ctx.expression())

        if not isinstance(index, int):
            print("runtime error")
            sys.exit(0)

        if index < 0 or index >= len(list_value):
            print("runtime error")
            sys.exit(0)

        return list_value[index]

    def visitExpressionListIndexExpr(
        self, ctx: EpicLangParser.ExpressionListIndexExprContext
    ):
        value = self.visit(ctx.expression())

        if not isinstance(value, list):
            print("runtime error")
            sys.exit(0)

        indices = ctx.indexSequence().expression()
        for index_expr in indices:
            index = self.visit(index_expr)

            if not isinstance(index, int):
                print("runtime error")
                sys.exit(0)

            # Проверяем границы списка
            if index < 0 or index >= len(value):
                print("runtime error")
                sys.exit(0)

            # Делаем шаг к следующему элементу
            value = value[index]

        return value


def main():
    # create input stream
    in_stream = FileStream(sys.argv[1])
    # in_stream = FileStream("code.txt")
    # create a lexer
    lexer = EpicLangLexer(in_stream)
    # for token in lexer.getAllTokens():
    #     print(f"Type: {token.type}, Text: '{token.text}'")
    # add error handling for our lexer
    lexer.addErrorListener(ErrorHandler())
    lexer.removeErrorListener(ConsoleErrorListener.INSTANCE)

    # create a parser with the lexer as an input
    stream = CommonTokenStream(lexer)

    parser = EpicLangParser(stream)
    # add error handling for our parser
    parser.addErrorListener(ErrorHandler())
    parser.removeErrorListener(ConsoleErrorListener.INSTANCE)

    # use the parser to obtain an abstract syntax tree
    tree = parser.program()
    # print(tree.toStringTree(recog=parser))

    visitor = EpicLang()
    visitor.visit(tree)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.exit(1)
