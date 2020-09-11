from .Tag import Tag
from .Token import Token

class Word(Token):

    def __init__(self, lexeme, tag):
        Token.__init__(self, tag)
        self.lexeme = lexeme

    def getLexeme(self):
        return self.lexeme
    
    def toString(self):
        return 'WORD - LEXEME = ' + self.lexeme
    
class WordA:
    def __init__(self):
        self.eq = Word('==', Tag.EQ)
        self.ne = Word('<>', Tag.NEQ)
        self.le = Word('<=', Tag.LE)
        self.ge = Word('>=', Tag.GE)
        self.minus = Word('minus', Tag.MINUS)
        self.assign = Word(':=', Tag.ASSIGN)
        self.true = Word('true', Tag.TRUE)
        self.false = Word('false', Tag.FALSE)
    
WordAux = WordA()