from dataclasses import dataclass

# Token types
# a dictionary stores key: value pairs,
TOKEN_TYPES = {
    'LET': 'LET',
    'IDENT': 'IDENT', # Identifier
    'NUMBER': 'NUMBER',
    'EQUAL': 'EQUAL',
    'PLUS': 'PLUS',
    'MINUS': 'MINUS',
    'MULTIPLY': 'MULTIPLY',
    'DIVIDE': 'DIVIDE',
    'SEMICOLON': 'SEMICOLON',
    'LPAREN': 'LPAREN',
    'RPAREN': 'RPAREN',
    'EOF': 'EOF'
}

@dataclass #saves you from writing boring boilerplate code, __init__, to initialise a class

class Token:
    type: str
    value: str
