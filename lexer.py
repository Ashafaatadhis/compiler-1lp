from sly import Lexer

class OneLLexer(Lexer):
    tokens = { ID, NUM, PRINT, ASSIGN, PLUS, MINUS, TIMES, DIV }
    ignore = ' \t'
    literals = { '(', ')', ',', ';' }

    PRINT = r'print'
    ASSIGN = r':='

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUM = r'\d+'

    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIV = r'/'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        self.index += 1
