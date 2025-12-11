from sly import Parser
from lexer import OneLLexer

class OneLParser(Parser):
    tokens = OneLLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIV),
    )

    @_('stm ";" stm')
    def stm(self, p):
        return ('seq', p.stm0, p.stm1)

    @_('ID ASSIGN exp')
    def stm(self, p):
        return ('assign', p.ID, p.exp)

    @_('PRINT "(" explist ")"')
    def stm(self, p):
        return ('print', p.explist)

    @_('ID')
    def exp(self, p):
        return ('id', p.ID)

    @_('NUM')
    def exp(self, p):
        return ('num', int(p.NUM))

    @_('exp PLUS exp')
    @_('exp MINUS exp')
    @_('exp TIMES exp')
    @_('exp DIV exp')
    def exp(self, p):
        return ('binop', p[1], p.exp0, p.exp1)

    @_('"(" stm "," exp ")"')
    def exp(self, p):
        return ('eseq', p.stm, p.exp)

    @_('exp "," explist')
    def explist(self, p):
        return [p.exp] + p.explist

    @_('exp')
    def explist(self, p):
        return [p.exp]
