from .Tag import Tag
from .Token import Token

class Integer(Token):

    def __init__(self, value):
        Token.__init__(self, Tag.INTEGER)
        self.value = value

    def getValue(self):
        return self.value

    def toString(self):
        return 'INTEGER - VALUE = ' + str(self.value)