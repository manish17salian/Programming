# Question: https://www.naukri.com/code360/problems/making-the-largest-island_1381282?leftPanelTabValue=PROBLEM

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])


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
        

        parent = list(range(row * col))
        size = [1] * (row * col)
        
        direction = [(0,1), (0,-1), (1,0), (-1,0)]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    continue
                
                for dr, dc in direction:
                    ndr = r+dr
                    ndc = c+dc
                    if 0<=ndr<row and 0<=ndc<col and grid[ndr][ndc] == 1:
                        node = r*row+c
                        adj_node = ndr*row+ndc
                        unionBySize(node, adj_node)
        
        max_Size = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    continue
                component = set()
                for dr, dc in direction:
                    ndr = dr+r
                    ndc = dc+c
                    if 0<=ndr<row and 0<=ndc<col and grid[ndr][ndc] == 1:
                        component.add(find(ndr*row+ndc))
                cm_size = 0  
                for node in component:
                    cm_size+=size[node]
                max_Size = max(max_Size, cm_size+1)
        
        for cell_no in range(row*col):
            max_Size = max(max_Size, size[find(cell_no)])

        return max_Size
            