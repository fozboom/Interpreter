# Generated from EpicLang.g4 by ANTLR 4.13.2
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
        4,1,45,233,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,51,8,1,1,1,1,1,1,1,
        1,2,1,2,1,2,5,2,59,8,2,10,2,12,2,62,9,2,1,3,1,3,5,3,66,8,3,10,3,
        12,3,69,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,94,8,4,1,5,1,5,1,5,1,
        6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,3,7,120,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,142,8,7,10,7,12,
        7,145,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,154,8,8,10,8,12,8,157,
        9,8,1,9,1,9,1,9,3,9,162,8,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,170,8,9,
        1,10,1,10,1,10,5,10,175,8,10,10,10,12,10,178,9,10,1,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,190,8,12,1,13,1,13,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        3,15,208,8,15,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,3,17,218,8,
        17,1,18,1,18,1,18,1,18,5,18,224,8,18,10,18,12,18,227,9,18,3,18,229,
        8,18,1,18,1,18,1,18,0,1,14,19,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,0,5,1,0,9,11,1,0,12,14,1,0,10,11,1,0,15,18,1,0,
        19,20,253,0,41,1,0,0,0,2,46,1,0,0,0,4,55,1,0,0,0,6,63,1,0,0,0,8,
        93,1,0,0,0,10,95,1,0,0,0,12,98,1,0,0,0,14,119,1,0,0,0,16,146,1,0,
        0,0,18,169,1,0,0,0,20,171,1,0,0,0,22,179,1,0,0,0,24,183,1,0,0,0,
        26,191,1,0,0,0,28,196,1,0,0,0,30,205,1,0,0,0,32,209,1,0,0,0,34,217,
        1,0,0,0,36,219,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,
        41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,
        0,0,1,45,1,1,0,0,0,46,47,5,25,0,0,47,48,5,43,0,0,48,50,5,1,0,0,49,
        51,3,4,2,0,50,49,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,53,5,2,0,
        0,53,54,3,6,3,0,54,3,1,0,0,0,55,60,5,43,0,0,56,57,5,3,0,0,57,59,
        5,43,0,0,58,56,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,
        61,5,1,0,0,0,62,60,1,0,0,0,63,67,5,4,0,0,64,66,3,8,4,0,65,64,1,0,
        0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,
        1,0,0,0,70,71,5,5,0,0,71,7,1,0,0,0,72,94,3,6,3,0,73,74,3,18,9,0,
        74,75,5,6,0,0,75,94,1,0,0,0,76,77,3,14,7,0,77,78,5,6,0,0,78,94,1,
        0,0,0,79,80,3,22,11,0,80,81,5,6,0,0,81,94,1,0,0,0,82,94,3,24,12,
        0,83,94,3,26,13,0,84,94,3,28,14,0,85,86,3,30,15,0,86,87,5,6,0,0,
        87,94,1,0,0,0,88,89,3,32,16,0,89,90,5,6,0,0,90,94,1,0,0,0,91,94,
        3,10,5,0,92,94,3,12,6,0,93,72,1,0,0,0,93,73,1,0,0,0,93,76,1,0,0,
        0,93,79,1,0,0,0,93,82,1,0,0,0,93,83,1,0,0,0,93,84,1,0,0,0,93,85,
        1,0,0,0,93,88,1,0,0,0,93,91,1,0,0,0,93,92,1,0,0,0,94,9,1,0,0,0,95,
        96,5,26,0,0,96,97,5,6,0,0,97,11,1,0,0,0,98,99,5,27,0,0,99,100,5,
        6,0,0,100,13,1,0,0,0,101,102,6,7,-1,0,102,103,5,43,0,0,103,120,3,
        16,8,0,104,120,3,34,17,0,105,120,3,36,18,0,106,107,3,36,18,0,107,
        108,5,7,0,0,108,109,3,14,7,0,109,110,5,8,0,0,110,120,1,0,0,0,111,
        112,7,0,0,0,112,120,3,14,7,10,113,114,5,1,0,0,114,115,3,14,7,0,115,
        116,5,2,0,0,116,120,1,0,0,0,117,120,3,18,9,0,118,120,5,43,0,0,119,
        101,1,0,0,0,119,104,1,0,0,0,119,105,1,0,0,0,119,106,1,0,0,0,119,
        111,1,0,0,0,119,113,1,0,0,0,119,117,1,0,0,0,119,118,1,0,0,0,120,
        143,1,0,0,0,121,122,10,8,0,0,122,123,7,1,0,0,123,142,3,14,7,9,124,
        125,10,7,0,0,125,126,7,2,0,0,126,142,3,14,7,8,127,128,10,6,0,0,128,
        129,7,3,0,0,129,142,3,14,7,7,130,131,10,5,0,0,131,132,7,4,0,0,132,
        142,3,14,7,6,133,134,10,4,0,0,134,135,5,21,0,0,135,142,3,14,7,5,
        136,137,10,3,0,0,137,138,5,22,0,0,138,142,3,14,7,4,139,140,10,14,
        0,0,140,142,3,16,8,0,141,121,1,0,0,0,141,124,1,0,0,0,141,127,1,0,
        0,0,141,130,1,0,0,0,141,133,1,0,0,0,141,136,1,0,0,0,141,139,1,0,
        0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,15,1,0,0,
        0,145,143,1,0,0,0,146,147,5,7,0,0,147,148,3,14,7,0,148,155,5,8,0,
        0,149,150,5,7,0,0,150,151,3,14,7,0,151,152,5,8,0,0,152,154,1,0,0,
        0,153,149,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,
        0,156,17,1,0,0,0,157,155,1,0,0,0,158,159,5,43,0,0,159,161,5,1,0,
        0,160,162,3,20,10,0,161,160,1,0,0,0,161,162,1,0,0,0,162,163,1,0,
        0,0,163,170,5,2,0,0,164,165,5,34,0,0,165,166,5,1,0,0,166,167,3,14,
        7,0,167,168,5,2,0,0,168,170,1,0,0,0,169,158,1,0,0,0,169,164,1,0,
        0,0,170,19,1,0,0,0,171,176,3,14,7,0,172,173,5,3,0,0,173,175,3,14,
        7,0,174,172,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,
        0,0,177,21,1,0,0,0,178,176,1,0,0,0,179,180,5,43,0,0,180,181,5,23,
        0,0,181,182,3,14,7,0,182,23,1,0,0,0,183,184,5,33,0,0,184,185,3,14,
        7,0,185,186,5,38,0,0,186,189,3,8,4,0,187,188,5,29,0,0,188,190,3,
        8,4,0,189,187,1,0,0,0,189,190,1,0,0,0,190,25,1,0,0,0,191,192,5,40,
        0,0,192,193,3,14,7,0,193,194,5,28,0,0,194,195,3,8,4,0,195,27,1,0,
        0,0,196,197,5,31,0,0,197,198,5,43,0,0,198,199,5,32,0,0,199,200,3,
        14,7,0,200,201,5,41,0,0,201,202,3,14,7,0,202,203,5,28,0,0,203,204,
        3,8,4,0,204,29,1,0,0,0,205,207,5,37,0,0,206,208,3,14,7,0,207,206,
        1,0,0,0,207,208,1,0,0,0,208,31,1,0,0,0,209,210,5,36,0,0,210,211,
        3,14,7,0,211,33,1,0,0,0,212,218,5,44,0,0,213,218,5,39,0,0,214,218,
        5,30,0,0,215,218,5,35,0,0,216,218,3,36,18,0,217,212,1,0,0,0,217,
        213,1,0,0,0,217,214,1,0,0,0,217,215,1,0,0,0,217,216,1,0,0,0,218,
        35,1,0,0,0,219,228,5,7,0,0,220,225,3,14,7,0,221,222,5,3,0,0,222,
        224,3,14,7,0,223,221,1,0,0,0,224,227,1,0,0,0,225,223,1,0,0,0,225,
        226,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,228,220,1,0,0,0,228,
        229,1,0,0,0,229,230,1,0,0,0,230,231,5,8,0,0,231,37,1,0,0,0,17,41,
        50,60,67,93,119,141,143,155,161,169,176,189,207,217,225,228
    ]

class EpicLangParser ( Parser ):

    grammarFileName = "EpicLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'{'", "'}'", "';'", 
                     "'['", "']'", "'!'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", "'&'", 
                     "'|'", "'='", "<INVALID>", "'func'", "'break'", "'continue'", 
                     "'do'", "'else'", "'false'", "'for'", "'in'", "'if'", 
                     "'len'", "'none'", "'print'", "'return'", "'then'", 
                     "'true'", "'while'", "'..'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WHITESPACE", "FUNC", "BREAK", "CONTINUE", "DO", "ELSE", 
                      "FALSE", "FOR", "IN", "IF", "LEN", "NONE", "PRINT", 
                      "RETURN", "THEN", "TRUE", "WHILE", "DOTS", "BOOL", 
                      "IDENTIFIER", "INT", "COMMENT" ]

    RULE_program = 0
    RULE_funcDef = 1
    RULE_params = 2
    RULE_block = 3
    RULE_statement = 4
    RULE_break = 5
    RULE_continue = 6
    RULE_expression = 7
    RULE_indexSequence = 8
    RULE_functionCall = 9
    RULE_argumentList = 10
    RULE_assignment = 11
    RULE_ifStatement = 12
    RULE_whileStatement = 13
    RULE_forStatement = 14
    RULE_returnStatement = 15
    RULE_printStatement = 16
    RULE_literal = 17
    RULE_listLiteral = 18

    ruleNames =  [ "program", "funcDef", "params", "block", "statement", 
                   "break", "continue", "expression", "indexSequence", "functionCall", 
                   "argumentList", "assignment", "ifStatement", "whileStatement", 
                   "forStatement", "returnStatement", "printStatement", 
                   "literal", "listLiteral" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    WHITESPACE=24
    FUNC=25
    BREAK=26
    CONTINUE=27
    DO=28
    ELSE=29
    FALSE=30
    FOR=31
    IN=32
    IF=33
    LEN=34
    NONE=35
    PRINT=36
    RETURN=37
    THEN=38
    TRUE=39
    WHILE=40
    DOTS=41
    BOOL=42
    IDENTIFIER=43
    INT=44
    COMMENT=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(EpicLangParser.EOF, 0)

        def funcDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EpicLangParser.FuncDefContext)
            else:
                return self.getTypedRuleContext(EpicLangParser.FuncDefContext,i)


        def getRuleIndex(self):
            return EpicLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = EpicLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 38
                self.funcDef()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(EpicLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(EpicLangParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(EpicLangParser.IDENTIFIER, 0)

        def block(self):
            return self.getTypedRuleContext(EpicLangParser.BlockContext,0)


        def params(self):
            return self.getTypedRuleContext(EpicLangParser.ParamsContext,0)


        def getRuleIndex(self):
            return EpicLangParser.RULE_funcDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDef" ):
                return visitor.visitFuncDef(self)
            else:
                return visitor.visitChildren(self)




    def funcDef(self):

        localctx = EpicLangParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(EpicLangParser.FUNC)
            self.state = 47
            self.match(EpicLangParser.IDENTIFIER)
            self.state = 48
            self.match(EpicLangParser.T__0)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 49
                self.params()


            self.state = 52
            self.match(EpicLangParser.T__1)
            self.state = 53
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(EpicLangParser.IDENTIFIER)
            else:
                return self.getToken(EpicLangParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return EpicLangParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = EpicLangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(EpicLangParser.IDENTIFIER)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 56
                self.match(EpicLangParser.T__2)
                self.state = 57
                self.match(EpicLangParser.IDENTIFIER)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EpicLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(EpicLangParser.StatementContext,i)


        def getRuleIndex(self):
            return EpicLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = EpicLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(EpicLangParser.T__3)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 28307257036434) != 0):
                self.state = 64
                self.statement()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(EpicLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(EpicLangParser.BlockContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(EpicLangParser.FunctionCallContext,0)


        def expression(self):
            return self.getTypedRuleContext(EpicLangParser.ExpressionContext,0)


        def assignment(self):
            return self.getTypedRuleContext(EpicLangParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(EpicLangParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(EpicLangParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(EpicLangParser.ForStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(EpicLangParser.ReturnStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(EpicLangParser.PrintStatementContext,0)


        def break_(self):
            return self.getTypedRuleContext(EpicLangParser.BreakContext,0)


        def continue_(self):
            return self.getTypedRuleContext(EpicLangParser.ContinueContext,0)


        def getRuleIndex(self):
            return EpicLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = EpicLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.functionCall()
                self.state = 74
                self.match(EpicLangParser.T__5)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.expression(0)
                self.state = 77
                self.match(EpicLangParser.T__5)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.assignment()
                self.state = 80
                self.match(EpicLangParser.T__5)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 82
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 83
                self.whileStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 84
                self.forStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 85
                self.returnStatement()
                self.state = 86
                self.match(EpicLangParser.T__5)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 88
                self.printStatement()
                self.state = 89
                self.match(EpicLangParser.T__5)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 91
                self.break_()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 92
                self.continue_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(EpicLangParser.BREAK, 0)

        def getRuleIndex(self):
            return EpicLangParser.RULE_break

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak" ):
                listener.enterBreak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak" ):
                listener.exitBreak(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak" ):
                return visitor.visitBreak(self)
            else:
                return visitor.visitChildren(self)




    def break_(self):

        localctx = EpicLangParser.BreakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(EpicLangParser.BREAK)
            self.state = 96
            self.match(EpicLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(EpicLangParser.CONTINUE, 0)

        def getRuleIndex(self):
            return EpicLangParser.RULE_continue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue" ):
                listener.enterContinue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue" ):
                listener.exitContinue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue" ):
                return visitor.visitContinue(self)
            else:
                return visitor.visitChildren(self)




    def continue_(self):

        localctx = EpicLangParser.ContinueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(EpicLangParser.CONTINUE)
            self.state = 99
            self.match(EpicLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EpicLangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EpicLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EpicLangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class ListLiteralIndexExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def listLiteral(self):
            return self.getTypedRuleContext(EpicLangParser.ListLiteralContext,0)

        def expression(self):
            return self.getTypedRuleContext(EpicLangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteralIndexExpr" ):
                listener.enterListLiteralIndexExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteralIndexExpr" ):
                listener.exitListLiteralIndexExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLiteralIndexExpr" ):
                return visitor.visitListLiteralIndexExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EpicLangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EpicLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EpicLangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(EpicLangParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpr" ):
                listener.enterFunctionCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpr" ):
                listener.exitFunctionCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpr" ):
                return visitor.visitFunctionCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EpicLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EpicLangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqualityExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EpicLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EpicLangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)


    class ListLiteralExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def listLiteral(self):
            return self.getTypedRuleContext(EpicLangParser.ListLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteralExpr" ):
                listener.enterListLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteralExpr" ):
                listener.exitListLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLiteralExpr" ):
                return visitor.visitListLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class CompareExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EpicLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EpicLangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareExpr" ):
                listener.enterCompareExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareExpr" ):
                listener.exitCompareExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareExpr" ):
                return visitor.visitCompareExpr(self)
            else:
                return visitor.visitChildren(self)


    class ListIndexExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(EpicLangParser.IDENTIFIER, 0)
        def indexSequence(self):
            return self.getTypedRuleContext(EpicLangParser.IndexSequenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListIndexExpr" ):
                listener.enterListIndexExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListIndexExpr" ):
                listener.exitListIndexExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListIndexExpr" ):
                return visitor.visitListIndexExpr(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(EpicLangParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpr" ):
                listener.enterLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpr" ):
                listener.exitLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class VarExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(EpicLangParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarExpr" ):
                listener.enterVarExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarExpr" ):
                listener.exitVarExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EpicLangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EpicLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EpicLangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionListIndexExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EpicLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EpicLangParser.ExpressionContext,0)

        def indexSequence(self):
            return self.getTypedRuleContext(EpicLangParser.IndexSequenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionListIndexExpr" ):
                listener.enterExpressionListIndexExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionListIndexExpr" ):
                listener.exitExpressionListIndexExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionListIndexExpr" ):
                return visitor.visitExpressionListIndexExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EpicLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = EpicLangParser.ListIndexExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 102
                self.match(EpicLangParser.IDENTIFIER)
                self.state = 103
                self.indexSequence()
                pass

            elif la_ == 2:
                localctx = EpicLangParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 104
                self.literal()
                pass

            elif la_ == 3:
                localctx = EpicLangParser.ListLiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 105
                self.listLiteral()
                pass

            elif la_ == 4:
                localctx = EpicLangParser.ListLiteralIndexExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.listLiteral()
                self.state = 107
                self.match(EpicLangParser.T__6)
                self.state = 108
                self.expression(0)
                self.state = 109
                self.match(EpicLangParser.T__7)
                pass

            elif la_ == 5:
                localctx = EpicLangParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 112
                self.expression(10)
                pass

            elif la_ == 6:
                localctx = EpicLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(EpicLangParser.T__0)
                self.state = 114
                self.expression(0)
                self.state = 115
                self.match(EpicLangParser.T__1)
                pass

            elif la_ == 7:
                localctx = EpicLangParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 117
                self.functionCall()
                pass

            elif la_ == 8:
                localctx = EpicLangParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 118
                self.match(EpicLangParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 141
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = EpicLangParser.MulDivExprContext(self, EpicLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 121
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 122
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 123
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = EpicLangParser.AddSubExprContext(self, EpicLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 124
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 125
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 126
                        self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = EpicLangParser.CompareExprContext(self, EpicLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 127
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 128
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 129
                        self.expression(7)
                        pass

                    elif la_ == 4:
                        localctx = EpicLangParser.EqualityExprContext(self, EpicLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 130
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 131
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 132
                        self.expression(6)
                        pass

                    elif la_ == 5:
                        localctx = EpicLangParser.AndExprContext(self, EpicLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 133
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 134
                        localctx.op = self.match(EpicLangParser.T__20)
                        self.state = 135
                        self.expression(5)
                        pass

                    elif la_ == 6:
                        localctx = EpicLangParser.OrExprContext(self, EpicLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 136
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 137
                        localctx.op = self.match(EpicLangParser.T__21)
                        self.state = 138
                        self.expression(4)
                        pass

                    elif la_ == 7:
                        localctx = EpicLangParser.ExpressionListIndexExprContext(self, EpicLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 139
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 140
                        self.indexSequence()
                        pass

             
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IndexSequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EpicLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EpicLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EpicLangParser.RULE_indexSequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexSequence" ):
                listener.enterIndexSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexSequence" ):
                listener.exitIndexSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexSequence" ):
                return visitor.visitIndexSequence(self)
            else:
                return visitor.visitChildren(self)




    def indexSequence(self):

        localctx = EpicLangParser.IndexSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_indexSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(EpicLangParser.T__6)
            self.state = 147
            self.expression(0)
            self.state = 148
            self.match(EpicLangParser.T__7)
            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 149
                    self.match(EpicLangParser.T__6)
                    self.state = 150
                    self.expression(0)
                    self.state = 151
                    self.match(EpicLangParser.T__7) 
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(EpicLangParser.IDENTIFIER, 0)

        def argumentList(self):
            return self.getTypedRuleContext(EpicLangParser.ArgumentListContext,0)


        def LEN(self):
            return self.getToken(EpicLangParser.LEN, 0)

        def expression(self):
            return self.getTypedRuleContext(EpicLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EpicLangParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = EpicLangParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(EpicLangParser.IDENTIFIER)
                self.state = 159
                self.match(EpicLangParser.T__0)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 26990648233602) != 0):
                    self.state = 160
                    self.argumentList()


                self.state = 163
                self.match(EpicLangParser.T__1)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(EpicLangParser.LEN)
                self.state = 165
                self.match(EpicLangParser.T__0)
                self.state = 166
                self.expression(0)
                self.state = 167
                self.match(EpicLangParser.T__1)
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


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EpicLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EpicLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EpicLangParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = EpicLangParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.expression(0)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 172
                self.match(EpicLangParser.T__2)
                self.state = 173
                self.expression(0)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(EpicLangParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(EpicLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EpicLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = EpicLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(EpicLangParser.IDENTIFIER)
            self.state = 180
            self.match(EpicLangParser.T__22)
            self.state = 181
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(EpicLangParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(EpicLangParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(EpicLangParser.THEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EpicLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(EpicLangParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(EpicLangParser.ELSE, 0)

        def getRuleIndex(self):
            return EpicLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = EpicLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(EpicLangParser.IF)
            self.state = 184
            self.expression(0)
            self.state = 185
            self.match(EpicLangParser.THEN)
            self.state = 186
            self.statement()
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 187
                self.match(EpicLangParser.ELSE)
                self.state = 188
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(EpicLangParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(EpicLangParser.ExpressionContext,0)


        def DO(self):
            return self.getToken(EpicLangParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(EpicLangParser.StatementContext,0)


        def getRuleIndex(self):
            return EpicLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = EpicLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(EpicLangParser.WHILE)
            self.state = 192
            self.expression(0)
            self.state = 193
            self.match(EpicLangParser.DO)
            self.state = 194
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(EpicLangParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(EpicLangParser.IDENTIFIER, 0)

        def IN(self):
            return self.getToken(EpicLangParser.IN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EpicLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EpicLangParser.ExpressionContext,i)


        def DOTS(self):
            return self.getToken(EpicLangParser.DOTS, 0)

        def DO(self):
            return self.getToken(EpicLangParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(EpicLangParser.StatementContext,0)


        def getRuleIndex(self):
            return EpicLangParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = EpicLangParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(EpicLangParser.FOR)
            self.state = 197
            self.match(EpicLangParser.IDENTIFIER)
            self.state = 198
            self.match(EpicLangParser.IN)
            self.state = 199
            self.expression(0)
            self.state = 200
            self.match(EpicLangParser.DOTS)
            self.state = 201
            self.expression(0)
            self.state = 202
            self.match(EpicLangParser.DO)
            self.state = 203
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(EpicLangParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(EpicLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EpicLangParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = EpicLangParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(EpicLangParser.RETURN)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 26990648233602) != 0):
                self.state = 206
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(EpicLangParser.PRINT, 0)

        def expression(self):
            return self.getTypedRuleContext(EpicLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EpicLangParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = EpicLangParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(EpicLangParser.PRINT)
            self.state = 210
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(EpicLangParser.INT, 0)

        def TRUE(self):
            return self.getToken(EpicLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(EpicLangParser.FALSE, 0)

        def NONE(self):
            return self.getToken(EpicLangParser.NONE, 0)

        def listLiteral(self):
            return self.getTypedRuleContext(EpicLangParser.ListLiteralContext,0)


        def getRuleIndex(self):
            return EpicLangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = EpicLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literal)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(EpicLangParser.INT)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(EpicLangParser.TRUE)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.match(EpicLangParser.FALSE)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 4)
                self.state = 215
                self.match(EpicLangParser.NONE)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 216
                self.listLiteral()
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


    class ListLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EpicLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EpicLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EpicLangParser.RULE_listLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteral" ):
                listener.enterListLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteral" ):
                listener.exitListLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLiteral" ):
                return visitor.visitListLiteral(self)
            else:
                return visitor.visitChildren(self)




    def listLiteral(self):

        localctx = EpicLangParser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(EpicLangParser.T__6)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 26990648233602) != 0):
                self.state = 220
                self.expression(0)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 221
                    self.match(EpicLangParser.T__2)
                    self.state = 222
                    self.expression(0)
                    self.state = 227
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 230
            self.match(EpicLangParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 14)
         




