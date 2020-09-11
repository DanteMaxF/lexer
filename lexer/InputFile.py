
class InputFile:
    
    def __init__(self, filename):
        try:
            file = open(filename)
            self.data = file.read()
        except FileNotFoundError as error:
            raise error

        self.size = len(self.data)
        self.position = 0
        self.lineNumber = 0
        self.columnNumber = 0

    def getChar(self):
        self.position += 1
        if (self.isEoF()):
            raise EOFError

        c = self.data[self.position]

        

        if (c == '\n'):
            self.columnNumber = 1
            self.lineNumber += 1
        else:
            self.columnNumber += 1

        return c     

        

    def toString(self):
        return self.data

    def peekChar(self):
        if (self.isEoF()):
            raise EOFError
        return self.data[self.position]

    def isEoF(self):
        return (self.position >= self.size)

    def isEoL(self):
        return (self.isEoF() or self.peekChar() ==  '\n')
        