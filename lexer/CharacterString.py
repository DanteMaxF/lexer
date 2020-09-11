from .Tag import Tag
from .Token import Token

class CharacterString(Token):

    def __init__(self, value):
        Token.__init__(self, Tag.CHARACTERSTRING)
        self.value = value

    def getValue(self):
        return self.value

    def toString(self):
        return 'STRING - VALUE = ' + self.value