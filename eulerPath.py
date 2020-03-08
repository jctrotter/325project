from collections import defaultdict

# Eulerian cycle: A path through a graph which starts and ends at the same vertex and includes every edge at least once
# Compare to Hamiltonian cycle, which includes every vertex at least once.

class eulerGraph:
    def __init__(self,nodes):
        self.v = nodes # number of vertices
        self.graph = defaultdict(list) # key = node num, values = neighboring node(s)
        self.path = []

def addEdge(G,u,v): 
    G.graph[u].append(v) 
    G.graph[v].append(u) 

def popEdge(G,u,v):
    for i, key in enumerate(G.graph[u]): 
        if key == v: 
            G.graph[u].pop(i) 
    for i, key in enumerate(G.graph[v]): 
        if key == u: 
            G.graph[v].pop(i) 

def depthFirstSearchTally(G, v, visited):
    tally = 1
    visited[v] = True
    for i in G.graph[v]: 
        if visited[i] == False: 
            tally = tally + depthFirstSearchTally(G, i, visited)          
    return tally 

def EdgeValid(G,u,v):
    # an edge is valid for travel if
    # - v is the only neighbor of u, or in other words, it's the only option
    # - if v is not the last one remaining and not a dead end

   
    if len(G.graph[u]) == 1:  # check if v is the only neighbor of u
        return True
    else: # check if v is not a bridge
        # get num vertices reachable from where we are
        visited = [False]*(G.v) 
        countPreStep = depthFirstSearchTally(G, u, visited)

        # remove, get num reachable vertices again.
        popEdge(G,u,v)
        visited = [False]*(G.v)
        countPostStep = depthFirstSearchTally(G, u, visited)

        # this is checking that if we traverse down this route, we can still return to where we started by essentially reverse-traversing the route
        
        # add edge back so everything doesn't break
        addEdge(G,u,v)

        # if count be > count2, it's a dead end. else we're good
        if countPreStep > countPostStep: 
            return False
        else:
            return True


def findPath(G, u):
    for v in G.graph[u]:
        if EdgeValid(G,u,v):        # If our candidate edge is valid  
            G.path.append([u,v])    #   append to path
            popEdge(G,u,v)          #   remove it so we don't visit it again
            findPath(G,v)           #   recur


def Fleury(G): # Fleury's algorithm
    # Find a node that is Eulerian and traverse from there. In context of our project, u should always be be 0? TODO when we integrate
    u = 0
    for i in range(0, G.v):
        if not len(G.graph[i]) % 2 == 0:
            u = i
            break
    
    findPath(G,u)

