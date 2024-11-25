grammar EpicLang;

WHITESPACE: [ \t\r\n]+ -> skip;

program
    : funcDef* EOF
    ;

funcDef
    : FUNC IDENTIFIER '(' params? ')' block
    ;

params
    : IDENTIFIER (',' IDENTIFIER)*
    ;

block
    : '{' statement* '}'
    ;

statement
    : block
    | functionCall ';'
    | expression ';'
    | assignment ';'
    | ifStatement
    | whileStatement
    | forStatement
    | returnStatement ';'
    | printStatement ';'
    | break
    | continue
    ;

break:
    BREAK ';'
    ;

continue:
    CONTINUE ';'
    ;


expression
    :IDENTIFIER indexSequence                       # ListIndexExpr
    | expression indexSequence                       # ExpressionListIndexExpr
    | literal                                        # LiteralExpr
    | listLiteral                                    # ListLiteralExpr
    | listLiteral '[' expression ']'                 # ListLiteralIndexExpr
    | op=('!' | '+' | '-') expression                # UnaryExpr
    | '(' expression ')'                             # ParenExpr
    | expression op=('*' | '/' | '%') expression     # MulDivExpr
    | expression op=('+' | '-') expression           # AddSubExpr
    | expression op=('<' | '<=' | '>' | '>=') expression # CompareExpr
    | expression op=('==' | '!=') expression         # EqualityExpr
    | expression op='&' expression                   # AndExpr
    | expression op='|' expression                   # OrExpr
    | functionCall                                   # FunctionCallExpr
    | IDENTIFIER                                     # VarExpr

    ;

indexSequence
    : '[' expression ']' ( '[' expression ']' )*
    ;

functionCall
    : IDENTIFIER '(' argumentList? ')'
    | LEN '(' expression ')'
    ;

argumentList
    : expression (',' expression)*
    ;

assignment
    : IDENTIFIER '=' expression
    ;

ifStatement
    : IF expression THEN statement (ELSE statement)?
    ;

whileStatement
    : WHILE expression DO statement
    ;

forStatement
    : FOR IDENTIFIER IN expression DOTS expression DO statement
    ;

returnStatement
    : RETURN expression?
    ;

printStatement
    : PRINT expression
    ;

literal
    : INT
    | TRUE
    | FALSE
    | NONE
    | listLiteral
    ;

listLiteral
    : '[' (expression (',' expression)*)? ']'
    ;


FUNC: 'func';


BREAK: 'break';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FOR: 'for';
IN: 'in';
IF: 'if';
LEN: 'len';
NONE: 'none';
PRINT: 'print';
RETURN: 'return';
THEN: 'then';
TRUE: 'true';
WHILE: 'while';
DOTS: '..';
BOOL: TRUE | FALSE;
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;





COMMENT: '//' ~[\r\n]* -> skip;