def TPL(Mat):
    total = 0
    for i in range(len(Mat)):
        for j in range(len(Mat)):
            total += Mat[i][j]

    return total

def APL(Mat, TPL):
    return TPL/(len(Mat)**2 - len(Mat))

def PLD(Mat, APL):
    Nr = 0 
    for i in range(len(Mat)):
        for j in range(len(Mat)):
            if Mat[i][j] == 1:
                Nr += Mat[i][j]
    return APL/(Nr//2)

f = open("input_matrix2.txt", "r")
rMat = []

"""
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
[0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
[0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
[0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
[0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
"""


for l in f:
    rMat.append(list(map(int, l.split())))
#print(*rMat, sep = ",\n")

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = 1e7
 
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
 
        #self.printSolution(dist)

        return dist


def getShortest():
    g = Graph(len(rMat))
    g.graph = rMat

    sMat = []
    for i in range(len(rMat)):
        sMat.append(g.dijkstra(i))

    print(*sMat, sep="\n")

    t = TPL(sMat)
    a = APL(sMat, t)
    p = PLD(sMat, a) 

    print("\nTPL:", t)
    print("APL:", a)
    print("PLD:", p)

getShortest()


