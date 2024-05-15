# Question: https://www.naukri.com/code360/problems/kruskal%E2%80%99s-minimum-spanning-tree-algorithm_1082553?leftPanelTabValue=SUBMISSION

from typing import List

def kruskalMST(n: int, edges: List[List[int]]) -> int:
    # adj = [[] for _ in range(len(edges))]
    weight_edge = [(w, u, v) for u, v, w in edges]

    # for u,v,w in edges:
    #     adj[u].append((v,w))
    #     adj[v].append((u,w))
        
    
    parent = list(range(n+1))
    size = [1]*(n+1)

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]
    
    def unionBySize(u,v):
        root_u = find(u)
        root_v = find(v)

        if root_u != root_v:
            if size[root_u] > size[root_v]:
                parent[root_v] = root_u 
                size[root_u]+=size[root_v]
            else:
                parent[root_u] = root_v
                size[root_v] += size[root_u]
    
    weight_edge.sort()

    mst_weight = 0
    edges_used = 0
    for w, u, v in weight_edge:
        if find(u) != find(v):
            unionBySize(u,v)
            mst_weight+=w
            edges_used += 1
            if edges_used == n-1:
                break
    
    return mst_weight
