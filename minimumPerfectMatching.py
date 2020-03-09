import math
import sys
import queue

def d(u, v):
    return round(math.sqrt((u[0]-v[0])*(u[0]-v[0])+(u[1]-v[1])*(u[1]-v[1])), 0)

class subgraph:
    def __init__(self, n, points, G):
        self.n = n
        self.adjList = {}
        self.key = {}
        self.points = points
        self.populate_edges(G)

    def populate_edges(self, G):
        edges = {}
        visited = []
        for k in range(0, len(self.points)):      # k = u pointer
            if not self.points[k] in edges.keys():
                edges[self.points[k]] = []
            for l in range(0, len(self.points)):  # l = v pointer
                if not self.points[l] in edges.keys():
                    edges[self.points[l]] = []
                u = [G.xCoord[self.points[k]], G.yCoord[self.points[k]]] # coords of node 1
                v = [G.xCoord[self.points[l]], G.yCoord[self.points[l]]] # coords of node 2
                if not k == l and not [k,l] in visited and not [l,k] in visited: # if we aren't comparing to self and we haven't already gone through u
                    w = d(u,v) 
                    edges[self.points[k]].append([l, w])
                    edges[self.points[l]].append([k, w])
                    visited.append([k,l])
                    visited.append([l,k])
            self.key[self.points[k]] = u
        self.adjList = edges


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
    
    