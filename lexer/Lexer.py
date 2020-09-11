from .Tag import Tag
from .Word import Word, WordAux
from .InputFile import InputFile
from .CharacterString import CharacterString
from .Token import Token
from .Integer import Integer
from .Real import Real

def listToString(s):
    str1 = ""  
    
    for ele in s:  
        str1 += ele   
    
    return str1  
         

class Lexer:

    def __init__(self, filename):
        try:
            self.inputF = InputFile(filename)
        except FileNotFoundError as error:
             raise error
        self.peek = ' '
        self.words = {}
        
        self.reserve(Word('program', Tag.PROGRAM))
        self.reserve(Word('constante', Tag.CONSTANT))
        self.reserve(Word('var', Tag.VAR))
        self.reserve(Word('begin', Tag.BEGIN))
        self.reserve(Word('end', Tag.END))
        self.reserve(Word('integer', Tag.INTEGER))
        self.reserve(Word('real', Tag.REAL))
        self.reserve(Word('boolean', Tag.BOOLEAN))
        self.reserve(Word('string', Tag.STRING))
        self.reserve(Word('writeln', Tag.WRITELN))
        self.reserve(Word('readln', Tag.READLN))
        self.reserve(Word('while', Tag.WHILE))
        self.reserve(Word('do', Tag.DO))
        self.reserve(Word('repeat', Tag.REPEAT))
        self.reserve(Word('until', Tag.UNTIL))
        self.reserve(Word('for', Tag.FOR))
        self.reserve(Word('to', Tag.TO))
        self.reserve(Word('downto', Tag.DOWNTO))
        self.reserve(Word('if', Tag.IF))
        self.reserve(Word('then', Tag.THEN))
        self.reserve(Word('else', Tag.ELSE))
        self.reserve(Word('not', Tag.NOT))
        self.reserve(Word('div', Tag.DIV))
        self.reserve(Word('mod', Tag.MOD))
        self.reserve(Word('and', Tag.AND))
        self.reserve(Word('or', Tag.OR))

    def reserve(self, w):
        self.words[w.getLexeme()] = w

    def isReserverd(self, tkn):
        return (tkn.toString().lower() in self.words)
    
    def readCha(self):
        self.peek = self.inputF.getChar()

    def readCh(self, c):
        self.readCha()
        if (self.peek != c):
            return False
        return True
    
    def skipWhiteSpaces(self):
        self.peek = self.inputF.peekChar()
        while( self.peek.isspace() ):
            self.peek = self.inputF.getChar()

    def readCharacterString(self):
        cs = '' + self.peek

        self.peek = self.inputF.getChar()
        while (self.peek !=  "'"):
            cs += self.peek
            self.peek = self.inputF.getChar()
        cs  += self.peek
        self.readCha()
        return CharacterString(cs)

    def readComments(self):
        prev = self.inputF.position
        current = self.inputF.position + 1

        while ( (current < self.inputF.size) and (self.inputF.data[prev] != '*') and (self.inputF.data[current] != ')') ):
            prev = current
            current += 1
        
        if (current >= self.inputF.size):
            raise EOFError

        self.inputF.position = current + 1

        return Token(Tag.COMMENTS)

    def scan(self):
        self.skipWhiteSpaces()

        if (self.peek == '('):
            if ( self.readCh('*') ):
                self.readCha()
                return self.readComments()
            else:
                return Token('(')
        
        elif (self.peek == '<'):
            if ( self.readCh('=') ):
                return WordAux.le
            elif ( self.readCh('>') ):
                return WordAux.ne
            else:
                return Token('<')

        elif (self.peek == '>'):
            if ( self.readCh('=') ):
                return WordAux.ge
            else:
                return Token('>')

        elif (self.peek == '='):
            if ( self.readCh('=') ):
                return WordAux.eq
            else:
                return Token('=')
        
        elif (self.peek == ':'):
            if ( self.readCh('=') ):
                return WordAux.assign
            else:
                return Token(':')

        elif (self.peek == "'"):
            return self.readCharacterString()

        if (self.peek.isdigit()):
            v = 0
            while True:
                v = (10 * v) + int(self.peek)
                self.readCha()
                if not self.peek.isdigit():
                    break
            
            if (self.peek != '.'):
                return Integer(v)
            
            x = v
            d = 10

            while True:
                self.readCha()
                if (not self.peek.isdigit()):
                    break
                x = x + int(self.peek) / d
                d = d * 10
            
            return Real(x)

        if (self.peek.isalpha()):
            b = []

            while True:
                b.append(self.peek.lower())
                self.readCha()
                if (not self.peek.isidentifier()) and (not self.peek.isdigit()):
                    break
            
            s = listToString(b)
            w = self.words.get(s)
            if w != None:
                return w

            w = Word(s, Tag.ID)
            self.reserve(w)
            return w

        tok = Token(self.peek)
        self.readCha()
        return tok



    