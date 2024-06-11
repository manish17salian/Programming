# Question: https://leetcode.com/problems/number-of-islands/description/


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        island = 0

        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(r,c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in direction:
                    ndr = dr+row
                    ndc = dc+col
                    
                    if 0 <= ndr < rows and 0 <= ndc < cols and (ndr, ndc) not in visited and grid[ndr][ndc] == "1":
                        queue.append((ndr, ndc))
                        visited.add((ndr, ndc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    island+=1
        
        return island