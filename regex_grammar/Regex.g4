grammar Regex;

/** Top level entry point */
regex
    : unionExpr EOF
    ;

unionExpr
    : concatExpr ( '|' concatExpr )*
    ;

concatExpr
    : repeatExpr+
    ;

repeatExpr
    : atom postfix?
    ;

postfix
    : '*'
    | '+'
    | '?'
    ;

atom
    : DIGIT
    | '(' unionExpr ')'
    ;

DIGIT
    : [0-9]
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

