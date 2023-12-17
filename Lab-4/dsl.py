from ply import lex, yacc

# Define the tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
)

# Define token regex patterns
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# Define ignored characters (whitespace)
t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling for invalid characters
def t_error(t):
    print(f"Invalid character '{t.value[0]}'")
    t.lexer.skip(1)

# Parsing rules
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    if p[3] != 0:
        p[0] = p[1] / p[3]
    else:
        raise ZeroDivisionError("Division by zero")

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expression(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the lexer
lexer = lex.lex()

# Build the parser
parser = yacc.yacc()

# Test the DSL
def calculate(expression):
    return parser.parse(expression)

# Example usage
while True:
    try:
        expression = input("Enter an expression: ")
        result = calculate(expression)
        print("Result:", result)
    except EOFError:
        break
