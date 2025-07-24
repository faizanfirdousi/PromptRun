from lexer_token import TOKEN_TYPES, Token  # Assumes 'Token' is the class name

class Lexer:
    def __init__(self, source_code):
        self.code = source_code
        self.position = 0
        self.current_char = self.code[self.position] if self.code else None

    # method to increment the position
    def advance(self):
        self.position += 1
        if self.position < len(self.code):
            self.current_char = self.code[self.position]
        else:
            self.current_char = None

    # skipping the empty spaces
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '-'):
            result += self.current_char
            self.advance()

        if result == 'let':
            return Token(TOKEN_TYPES['LET'], result)
        else:
            return Token(TOKEN_TYPES['IDENT'], result)

    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        return Token(TOKEN_TYPES['NUMBER'], result)

    # storng the tokens
    def get_token(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()

            elif self.current_char.isalpha():
                tokens.append(self.identifier())

            elif self.current_char.isdigit():
                tokens.append(self.number())

            elif self.current_char == '=':
                tokens.append(Token(TOKEN_TYPES['EQUAL'],'='))
                self.advance()

            elif self.current_char == '+':
                tokens.append(Token(TOKEN_TYPES['PLUS'],'+'))
                self.advance()

            elif self.current_char == ';':
                tokens.append(Token(TOKEN_TYPES['SEMICOLON'], ';'))
                self.advance()

            else:
                raise Exception(f'Unkown character: {self.current_char}')


        tokens.append(Token(TOKEN_TYPES['EOF'],''))
        return tokens

