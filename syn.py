import ply.yacc as yacc
import ply.lex as lex

# Define the tokens
tokens = (
    'ACTION',
    'ENTITY',
    'RELATION',
    'MODIFIER',
    'SPECIFIC',
    'GROUP',
    'IDENTIFIER',  # General identifier token
)

# Define the expressions for each token
def t_ACTION(t):
    r'ختار|سال|اخدم|ضرب|أش|خبز|je|لاس'
    t.value = t.value  # Set the token value to the matched string
    return t

def t_ENTITY(t):
    r'الجار|المجرب|يا|بغي|الحديد|خاصك|الدار'
    t.value = t.value
    return t

def t_RELATION(t):
    r'قبل|وماتسال|صغري|لعسل|ماحدو|العريان|ياكلو'
    t.value = t.value
    return t

def t_MODIFIER(t):
    r'سخون|خاتم|البراني'
    t.value = t.value
    return t

def t_SPECIFIC(t):
    r'آمولاي|لقريص|كبري'
    t.value = t.value
    return t

def t_GROUP(t):
    r'النحل'
    t.value = t.value
    return t

# General identifier token
def t_IDENTIFIER(t):
    r'[^\s]+'
    t.value = t.value
    return t

# Ignore spaces
t_ignore = ' '

# Error handling for lexer
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define the start symbol
start = 'sentence'

# Define the grammar rules
# Define the grammar rules
def p_sentence(p):
    '''
    sentence : ACTION ENTITY RELATION MODIFIER SPECIFIC GROUP
             | ACTION ENTITY RELATION MODIFIER SPECIFIC
             | ACTION ENTITY RELATION MODIFIER
             | ACTION ENTITY RELATION
             | ACTION ENTITY
             | ACTION
    '''
    print("Parsed Sentence")

# Error handling for parser
def p_error(p):
    print("Syntax error")

# Build the parser
parser = yacc.yacc()




def test_lexer(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok.value,end=' ')
    print('\n')

# Function to test the parser with examples
def test_parser(input_string):
    test_lexer(input_string)
    parser.parse(input_string)

# Test the parser with examples
test_parser("je")
