#!/usr/bin/env python3
import sys



#Takes in cli test input.
def processInput():
    testFileName = sys.argv[1]
    print("This is test file: " + testFileName)
    testFile = open(testFileName)




    testFile.close()

def formatOutput():
    return None

def main():
    processInput()

if __name__ == "__main__":
    main()