from .Tag import Tag
from .Token import Token

class Real(Token):

    def __init__(self, value):
        Token.__init__(self, Tag.REAL)
        self.value = value

    def getValue(self):
        return self.value

    def toString(self):
        return 'REAL - VALUE = ' + str(self.value)