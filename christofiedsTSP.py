#!/usr/bin/env python3
import sys
import math

class InputGraph:

    def __init__(self):
        self.cityN = []
        self.cityDistances = [[0 for x in range(5000)] for y in range(5000)]
        self.xCoord = []
        self.yCoord = []
        self.testFileName = None


#Takes in cli test input.
def processInput(graphInput):
    testFileName = sys.argv[1]
    graphInput.testFileName = testFileName          #Save fileName for output file
    #print("This is test file: " + testFileName)

    #Loop through file. " " - cityN - cityX -cityY
    with open(testFileName) as inputFile:
        for line in inputFile:
            readIn = line.strip().split()
            cityVertex = int(readIn[0])
            cityX = int(readIn[1])
            cityY = int(readIn[2])
            #print("CityN--" + str(cityVertex) + "--xCoord--" + str(cityX) + "--yCoord--" + str(cityY))
            graphInput.cityN.append(cityVertex)
            graphInput.xCoord.append(cityX)
            graphInput.yCoord.append(cityY)
            #print(readIn)
def euclidCalc(graphInput):
    vertexCnt = len(graphInput.cityN)
    #print("Amount of vertices: " + str(vertexCnt))
    for u in range(vertexCnt):

        for v in range(vertexCnt):
            xVal1 = graphInput.xCoord[u]
            yVal1 = graphInput.yCoord[u]

            xVal2 = graphInput.xCoord[v]
            yVal2 = graphInput.yCoord[v]

            #Calculate distance
            distance = round(math.sqrt((xVal1-xVal2)**2 + (yVal1-yVal2)**2))
            #print("(x1,y1)<->(x2,y2): " + "("+ str(xVal1)+ ","+str(yVal1)+")"+ "("+ str(xVal2)+ ","+str(yVal2)+")"" distance: " + str(distance))
            #Put distance in distance 2D array
            graphInput.cityDistances[u][v] = distance   

def formatOutput(output):
    outputFileName = output.testFileName + ".tour"
    #print(outputFileName)
    #First line length of tour
    #n lines city idetifiers in order visited by tour

    return None

def main():
    tspGraph = InputGraph()                         #Instantiate InputGraph
    processInput(tspGraph)
    
    #Calculate distance between all city Vertices
    euclidCalc(tspGraph)
    #create MST
    
    #Format output
    formatOutput(tspGraph)

if __name__ == "__main__":
    main()