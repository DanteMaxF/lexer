import sys

from lexer.Tag import Tag
from lexer.Token import Token
from lexer.Integer import Integer
from lexer.CharacterString import CharacterString
from lexer.Real import Real
from lexer.Lexer import Lexer
from lexer.InputFile import InputFile
from lexer.Tag4Parser import tag4Parser
from myParser.Parser import Parser

debug = False

def main():

    commentsFound = 0

    if (len(sys.argv) != 2):
        print('usage: python Main.py file')
        return -1
    
    try:
        lex = Lexer(sys.argv[1])
    except FileNotFoundError:
        print('File not found')
        return -1

    if debug:
        print('### PROGRAM WILL START ###\n')

    line = lex.inputF.lineNumber + commentsFound
    column = lex.inputF.columnNumber
    token = lex.scan()
    
    tokens = []
    token2add = ''
    try:
        while True:
            if debug:
                print('' + token.toString() + '\t\t', end = '' )
            if token.tag != 292:
                if isinstance(token.tag, int):    
                    token2add = tag4Parser[token.tag]    
                else:
                    token2add = token.tag
                tokens.append([token2add, column, line])
                if debug:
                    print(token2add, end = '\t' )
            else:
                commentsFound += 1
            if debug:
                print()

            line = lex.inputF.lineNumber + commentsFound
            column = lex.inputF.columnNumber
            token = lex.scan()
    except Exception as error:
        pass

    eofToken = ['$', lex.inputF.lineNumber, lex.inputF.columnNumber]

    if debug:
        print("### END ###")
  
    myParser = Parser('myParser/table.csv', 'myParser/grammar.csv', tokens, eofToken)
    
    try:
        myParser.analyze()
        print('All good')
    except SyntaxError as error:
        print(error)
    

if __name__ == "__main__":
    main()