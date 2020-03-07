#!/usr/bin/env python3
import sys


class InputGraph:

    def __init__(self):
        self.cityN = []
        self.xCoord = []
        self.yCoord = []
        self.testFileName = None


#Takes in cli test input.
def processInput(graphInput):
    testFileName = sys.argv[1]
    graphInput.testFileName = testFileName          #Save fileName for output file
    print("This is test file: " + testFileName)

    #Loop through file. " " - cityN - cityX -cityY
    with open(testFileName) as inputFile:
        i = 0
        for line in inputFile:
            readIn = line.strip().split()
            cityVertex = readIn[0]
            cityX = readIn[1]
            cityY = readIn[2]
            print("CityN--" + str(cityVertex) + "--xCoord--" + str(cityX) + "--yCoord--" + str(cityY))
            graphInput.cityN.append(cityVertex)
            graphInput.xCoord.append(cityX)
            graphInput.yCoord.append(cityY)
            print(readIn)
            i += 1

def formatOutput():
    return None

def main():
    tspGraph = InputGraph()                         #Instantiate InputGraph
    processInput(tspGraph)
    
    #Calculate distance between all city Vertices

    #create MST
    #

if __name__ == "__main__":
    main()