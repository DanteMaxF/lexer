import sys
import numpy as np
import csv

class Parser:

    

    def __init__(self, tableFile, grammarFile, tokens, eofToken):
        self.actionDict = {} 
        self.gotoDict = {}
        self.readTable(tableFile)
        self.productions = self.readCSV(grammarFile)
        self.tokens = tokens
        self.tokens.append(eofToken)
        self.stack = ['0']

        self.debug = False

    def analyze(self):
        self.tokens = self.tokens[::-1] # Reverse token list
        
        if self.debug:
            print('Stack:', self.stack)

        while True:
            tkn = self.tokens[-1]

            if self.debug:
                print('input:', self.tokens[::-1][0])

            state = int(self.stack[-1])

            tableResult = self.actionDict[tkn[0]][state]
            if (tableResult == ''):
                errorTkn = tkn[0]
                if (tkn[0] == '$'):
                    errorTkn = 'EOF'
                raise SyntaxError('Error at:' +'(' + str(tkn[1]) + ',' + str(tkn[2]) + '): ' + errorTkn)

            if self.debug:
                print('action:', tableResult)
                print('----------------------------------')

            if tableResult == 'acc':
                break
            else:
                action = tableResult[0]
                actionNumber = tableResult[1:]

                if action == 's':
                    token = self.tokens.pop()
                    self.stack.append(token[0])
                    self.stack.append(actionNumber)
                    if self.debug:
                        print('Stack:', self.stack)
                
                elif action == 'r':
                    production = self.productions[int(actionNumber)]

                    if self.debug:
                        print(production)

                    elementsToRemove = len(production[1].split(' ')) * 2
                    if production[1] == '':
                        elementsToRemove = 0

                    for i in range(elementsToRemove):
                        self.stack.pop()

                    self.stack.append(production[0])

                    if self.debug:
                        print('Stack:', self.stack)
                        print('input:', self.tokens[::-1][0])

                    gotoState = self.gotoDict[self.stack[-1]][int(self.stack[-2])]
                    if self.debug:
                        print('goto:', gotoState)
                        print('----------------------------------')
                    self.stack.append(gotoState)
                    if self.debug:
                        print('Stack:', self.stack)
                else:
                    if (tkn[0] == '$'):
                        tkn[0] == 'end of file'
                    raise SyntaxError('Error at:' +'(' + str(tkn[1]) + ',' + str(tkn[2]) + '): ' + tkn[0])

    def readCSV(self, filename):
        reader = csv.reader(open(filename, 'r'), delimiter=',')
        return list(reader)

    def readTable(self, filename):
        x = self.readCSV(filename)
        data = np.array(self.readCSV(filename))
        # save action and goto into dictionaries

        state = data[2:,0]
        action = np.transpose(data[1:,1:47])

        for i in action:
            self.actionDict[i[0]] = i[1:]

        goto = np.transpose(data[1:,47:])

        for i in goto:
            self.gotoDict[i[0]] = i[1:]


# def main():
#     tokens = [ # TODO: Read tokens from Lexer
#         'program',
#         'identifier',
#         ';',
#         'begin',
#         'writeln',
#         '(',
#         'string',
#         ')',
#         ';',
#         'end',
#         '.',
#         '$'
#     ]

#     myParser = Parser('table.csv', 'grammar.csv', tokens)
#     myParser.analyze()   
    


# if __name__ == '__main__':
#     main()