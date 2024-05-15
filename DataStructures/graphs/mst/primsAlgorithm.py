from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

import heapq

# Edge class for storing the Edges of thee graph
class Edge:
    
    def __init__(self, start, end, weight) :

        self.start = start
        self.end = end
        self.weigth = weight


def minimumSpanningTree(edges, V, E):
    adj = [[] for _ in range(V)]

    for edge in edges:
        u, v, w = edge.start, edge.end, edge.weigth
        adj[u].append((v, w))
        adj[v].append((u, w))
    heap = []
    heapq.heappush(heap,(0,0,-1))
    visited = [0]*V
    minSum = 0
    mst = []

    while heap:
        weight, node, parent = heapq.heappop(heap)
        if visited[node] == 1: continue

        visited[node] = 1
        minSum += weight
        if parent != -1:
            mst.append((node, parent))

        for conn, wei in adj[node]:
            if visited[conn] == 0:
                heapq.heappush(heap, (wei, conn, parent))

    return minSum































#taking inpit using fast I/O
def takeInput() :
    n_m = stdin.readline().strip().split(" ")
    V = int(n_m[0].strip())
    E = int(n_m[1].strip())

    edges = [Edge(0, 0, 0) for i in range(E)]
    for i in range(E) :

        temp = list(map(int, stdin.readline().strip().split(" ")))
        edges[i] = Edge(temp[0], temp[1], temp[2])

    return edges, V, E


#main
edges, V, E = takeInput()
print(minimumSpanningTree(edges, V, E))
 