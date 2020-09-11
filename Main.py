import sys

from lexer.Tag import Tag
from lexer.Token import Token
from lexer.Integer import Integer
from lexer.CharacterString import CharacterString
from lexer.Real import Real
from lexer.Lexer import Lexer
from lexer.InputFile import InputFile

def main():
    if (len(sys.argv) != 2):
        print('usage: python Main.py file')
        return -1
    
    try:
        lex = Lexer(sys.argv[1])
    except FileNotFoundError:
        print('File not found')
        return -1


    print('### PROGRAM WILL START ###\n')
    token = lex.scan()
    try:
        while True:
            print('' + token.toString())
            token = lex.scan()
    except Exception as error:
        print(error)
        pass
    print("### END ###")

if __name__ == "__main__":
    main()