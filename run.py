from lexer_token import TOKEN_TYPES, Token 
from lexer import Lexer

source_code = "let x = 5 + 1;"
lexer = Lexer(source_code)
tokens = lexer.get_token()

for token in tokens:
    print(token)
