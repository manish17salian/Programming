# Question: https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/


from typing import List

def numberOfIslandII(n: int, m: int, queries: List[List[int]], q: int)-> int:
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
                size[root_u]+= size[root_v]
            else:
                parent[root_u] = root_v
                size[root_v]+= size[root_u]
    

    visited = [[0]*m for _ in range(n)]
    parent = list(range((n*m)+1))
    size = [1]*((n*m)+1)

    count = 0
    answer = []

    direction = [(0,1),(0,-1),(1,0), (-1,0)]

    for row, col in queries:

        if visited[row][col] == 1:
            answer.append(count)
            continue
        
        visited[row][col] = 1
        count+=1

        for dr, dc in direction:
            ndr = dr+row
            ndc = dc+col
            
            if 0<=ndr<n and 0<=ndc<m and visited[ndr][ndc] == 1:
                node_no = row * m + col
                adj_node_no = ndr * m + ndc
                if find(node_no) != find(adj_node_no):
                    unionBySize(node_no, adj_node_no)
                    count-=1
        
        answer.append(count)
    return answer
