import math
from operator import itemgetter

    
def d(u, v):
    return round(math.sqrt((u[0]-v[0])*(u[0]-v[0])+(u[1]-v[1])*(u[1]-v[1])), 0)

class graph:
    def __init__(self, n, points):
        self.n = n
        self.graph = []
        self.sorted_graph = []
        self.points = points
        self.key = {}
        self.mst = []
        self.mst_distance = 0
        self.populate_edges()


    def populate_edges(self):
        edges = []
        visited = []
        for k in range(0, len(self.points)):      # k = u pointer
            for l in range(0, len(self.points)):  # l = v pointer
                u = self.points[k]
                v = self.points[l]
                if not k == l and not [k,l] in visited and not [l,k] in visited: # if we aren't comparing to self and we haven't already gone through u
                    w = d(u,v) 
                    edges.append([k,l,w])
                    visited.append([k,l])
                    visited.append([l,k])
            self.key[k] = u  
        self.graph = edges

    def sort_set(self):
        self.sorted_graph = sorted(self.graph, key=itemgetter(2))

def find_set(parent, i): 
    if parent[i] == i: 
        return i 
    return find_set(parent, parent[i]) 

def U(parent, rank, x, y): 
    # union by rank
    root_x = find_set(parent, x) # find node x 
    root_y = find_set(parent, y) # find node y
    if rank[root_x] < rank[root_y]: # if x would be lower than y on the tree,
        parent[root_x] = root_y         # set y to be x's parent
    elif rank[root_x] > rank[root_y]: # if y would be lower than x on the tree,
        parent[root_y] = root_x         # set x to be y's parent
    else : 
        parent[root_y] = root_x    # otherwise we move x up a level in the tree, set y's parent to x
        rank[root_x] += 1
        
def Kruskal(graph):
    graph.sort_set()
    A = []
    edge = 0
    parent = []     # stores parent location for object at index i
    rank = []       # height of object at index i

    #init union by rank parent and rank arrays
    for n in range(len(graph.sorted_graph)): 
        parent.append(n)    # init all are own parent, unassigned
        rank.append(0)      # init all level 

    i = 0
    while edge < len(graph.sorted_graph)-1 and i < len(graph.sorted_graph):
        u,v,w = graph.sorted_graph[i]
        x = find_set(parent, u) # find set with u
        y = find_set(parent, v) # find set with v
        if not x == y:          # if union of u and v doesn't close (cycle), append, do the union
          edge = edge + 1
          A.append([u,v,w])
          U(parent, rank, x, y)
        i = i + 1

    toPrint = []
    running_w = 0
    for u,v,w in A: 
        print(str(graph.key[u]) + "\t---->\t" + str(graph.key[v]) + "    \t" + str(w))
        running_w += w
    print("Total distance:\t\t\t" + str(running_w))
    graph.mst = A
    graph.mst_distance = running_w

# driver
def debugDriver():
    fp = open("graph.txt") #TODO VALIDATE
    line = int(fp.readline())
    n = line
    points = []
    for i in range(0,n):
        line = fp.readline()
        coords = line.split(" ")
        for j in range(0, len(coords)):
            coords[j] = coords[j].replace('.','')
            coords[j] = coords[j].replace('\n','')
            coords[j] = int(coords[j])
        points.append(coords)
    graph = graph(n,points)
    Kruskal(graph)

