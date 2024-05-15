# Question: https://www.naukri.com/code360/problems/-most-stones-removed-with-same-row-or-column_1376597?leftPanelTabValue=PROBLEM

from typing import List

def countSquares(stones: List[List[int]]) -> int:


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
                size[root_u] = size[root_v]
            else:
                parent[root_u] = root_v
                size[root_v] = size[root_u]
    

    maxRow = max(stone[0] for stone in stones)
    maxCol = max(stone[1] for stone in stones)
    n = maxRow + maxCol + 1
    size = [1]*(n+1)
    parent = list(range(n+1))
    components = set()

    for  stone in stones:
        nodeRow = stone[0]
        nodeCol = stone[1] + maxRow + 1
        unionBySize(nodeRow, nodeCol)
        components.add(nodeRow)
        components.add(nodeCol)
    
    loneNodes = 0
    for i in components:
        if find(i) == i:
            loneNodes+=1
    
    return len(stones)-loneNodes
