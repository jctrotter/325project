#!/usr/bin/env python3
import sys
import math
from mstEuclid import *
from minimumPerfectMatching import *

class InputGraph:

    def __init__(self):
        self.cityN = []
        self.cityDistances = [[0 for x in range(5000)] for y in range(5000)]
        self.xCoord = []
        self.yCoord = []
        self.testFileName = None

        self.mst = []
        # - MST FORMAT -
        # list of [u, v, w]
        # u: start node n at xCoord[u] and yCoord[u]
        # v: end node v at xCoord[v] and yCoord[v]
        # w: weight of edge
        # sorted using Kruskals, in order of ascending path weight.
        self.mst_distance = 0

        self.euler = []


#Takes in cli test input.
def processInput(graphInput):
    #testFileName = sys.argv[1]
    testFileName = "test-input-1.txt"
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


def generateMST(inputG):
    # convert InputGraph from christofidesTSP to graph
    points = []
    for n in range(0, len(inputG.xCoord)):
        points.append([inputG.xCoord[n], inputG.yCoord[n]])
    tempGraph = graph(len(inputG.cityN), points)

    # run
    Kruskal(tempGraph)

    # return values
    inputG.mst = tempGraph.mst
    inputG.mst_distance = tempGraph.mst_distance

def main():
    tspGraph = InputGraph()                         #Instantiate InputGraph
    processInput(tspGraph)
    
    #Calculate distance between all city Vertices
    euclidCalc(tspGraph)
    #create MST
    generateMST(tspGraph)

    # Calculate set of vertices O with odd degree in T;
    O = generateOddVertices(tspGraph)
    # print(tspGraph.subgraph)
    # print(tspGraph.mst)

    # Construct a minimum-weight perfect matching M in this subgraph.
    generateMinPerfectMatch(tspGraph, O)
    print(tspGraph.euler)

    #Format output
    formatOutput(tspGraph)

if __name__ == "__main__":
    main()