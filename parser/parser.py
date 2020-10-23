import sys
import numpy as np
import csv

def main():
    reader = csv.reader(open("table.csv", "r"), delimiter=",")
    x = list(reader)
    data = np.array(x)
    # save action and goto into dictionaries
    
    state = data[2:,0]
    action = np.transpose(data[1:,1:49])
    actionDict = {}

    for i in action:
        actionDict[i[0]] = i[1:]

    goto = np.transpose(data[1:,49:])
    gotoDict = {}

    for i in goto:
        gotoDict[i[0]] = i[1:]

    


if __name__ == "__main__":
    main()