import math
import sys
import queue

def generateOddVertices(G):

    # get degrees of each node in the MST
    nodeDegrees = dict()

    # edge in format [u, v, w]
    # u is start node
    # v is the end node
    # w is the weight
    for edge in G.mst:
        startNode = edge[0]
        endNode = edge[1]

        if startNode in nodeDegrees.keys():
            nodeDegrees[startNode] += 1
        else:
            nodeDegrees[startNode] = 1

        if endNode in nodeDegrees.keys():
            nodeDegrees[endNode] += 1
        else:
            nodeDegrees[endNode] = 1

    O = [] # set of vertices with odd degree in MST
    for node in nodeDegrees.keys():
        if nodeDegrees[node] % 2 == 1:
            O.append(node)
    
    return O

def generateMinPerfectMatch(G, O):
    # find the minimum across all edges
    while O:
        v = O.pop()
        length = float("inf")
        u = 1
        closest = 0
        for u in O:
            if v != u and G.cityDistances[v][u] < length:
                length = float(G.cityDistances[v][u])
                closest = u
        
        if not [v, closest, length] in G.mst and not [closest, v, length] in G.mst:
            G.mst.append([v, closest, length])
        O.remove(closest)
    
    