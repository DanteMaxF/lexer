import sys
import numpy as np
import csv



def readTable(filename):
    x = readCSV(filename)
    data = np.array(x)
    # save action and goto into dictionaries

    state = data[2:,0]
    action = np.transpose(data[1:,1:47])
    actionDict = {}

    for i in action:
        actionDict[i[0]] = i[1:]

    goto = np.transpose(data[1:,47:])
    gotoDict = {}

    for i in goto:
        gotoDict[i[0]] = i[1:]
    
    return actionDict, gotoDict

def readCSV(filename):
    reader = csv.reader(open(filename, 'r'), delimiter=',')
    return list(reader)

def printLog(log):
    for i in log:
        for o in i:
            print(str(o)+'\t', end='')
        print('')

def main():

    actionDict, gotoDict = readTable('table.csv')
    productions = readCSV('grammar.csv')

    tokens = [ # TODO: Read tokens from Lexer
        'program',
        'identifier',
        ';',
        'begin',
        'writeln',
        '(',
        'string',
        ')',
        ';',
        'end',
        '.',
        '$'
    ]

    stack = ['0']

    tokens = tokens[::-1] # Reverse token list

    print('Stack:', stack)

    while True:
        tkn = tokens[-1]
        print('input:', tokens[::-1])

        state = int(stack[-1])

        tableResult = actionDict[tkn][state]
        print('action:', tableResult)
        print('----------------------------------')

        if tableResult == 'acc':
            break
        else:
            action = tableResult[0]
            actionNumber = tableResult[1:]

            if action == 's':
                token = tokens.pop()
                stack.append(token)
                stack.append(actionNumber)
                print('Stack:',stack)
            
            elif action == 'r':
                production = productions[int(actionNumber)]
                print(production)
                elementsToRemove = len(production[1].split(' ')) * 2
                if production[1] == '':
                    elementsToRemove = 0

                for i in range(elementsToRemove):
                    stack.pop()

                stack.append(production[0])
                print('Stack:', stack)
                print('input:', tokens[::-1])

                gotoState = gotoDict[stack[-1]][int(stack[-2])]
                print('goto:', gotoState)
                print('----------------------------------')
                stack.append(gotoState)
                print('Stack:', stack)
            else:
                print('ERROR DE GRAMÁTICA')



    


    
    


if __name__ == '__main__':
    main()