
# Nodes creating
class Numbernode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f'{self.tok}'
    
class BinOp:
    def __init__(self, left,op,right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f'({self.left}, {self.op}, {self.right})'

# Parser

class Parser:
    def __init__(tokens):
        self.tokens = tokens
        self.index = 1
        self.advance()

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        return self.current_token
    
    def parse(self):
        res = self.expr()
        return res

    def factor(self):
        tok = self.current_token

        if tok.type in (TT_INT , TT_FLOAT):
            self.advance()
            return Numbernode(tok)
        
    def term(self):
        return self.bin_op(self.factor, (TT_MUL , TT_DIV))
        
    def expr(self):
        return self.bin_op(self.term, (TT_PLUS, TT_MINUS))
        
        
    def bin_op(self, func, ops):
        left = func()
        while self.current_token.type in ops:
            op_token = self.current_token
            self.advance()
            right = func()
            left = BinOp(left , op_token , right)
        return left
    
# RUN 

def run(fn, text):

    # for generating tokens
    lexer = Lexer(fn, text)
    tokens,error = lexer.make_tokens()
    if error: return None, error

    # for generating syntac tree

    parser = Parser(tokens)
    ast = parser.parse()
    return ast , None