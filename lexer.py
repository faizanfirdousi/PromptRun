from token import TOKEN_TYPES, token #imports the TOKEN_TYPES dictionary from token.py

class lexer:
    def __init__(self, source_code):
        self.code = source_code
        self.position = 0
        self.current_char = self.code[self.postition] if self.code else None


    def advance(self):
        self.position += 1
        if self.position < len(self.code):
            self.current_char = self.code[self.postion]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance
