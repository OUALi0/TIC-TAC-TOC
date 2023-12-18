from ply import lex

# Liste des noms des jetons
tokens = (
    'WORD',
    'CONJUNCTION',
)

# Expression régulière pour les mots arabes
def t_WORD(t):
    r'دير|عين|شافت|عين|ماشافت'
    return t

# Expression régulière pour la conjonction "و"
def t_CONJUNCTION(t):
    r'و'
    return t

# Ignorer les espaces et les tabulations
t_ignore = ' \t'

# Gérer les erreurs
def t_error(t):
    print(f"Caractère illégal : {t.value[0]}")
    t.lexer.skip(1)

# Créer l'analyseur lexical
lexer = lex.lex()

# Fonction de test
def test_lexer(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok.value,end=' ')
        

# Test de l'analyseur lexical
test_lexer("دير عين شافت وعين ماشافت")