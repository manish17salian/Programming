# Question: https://leetcode.com/problems/max-area-of-island/description/

def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # rows = len(grid)
        # cols = len(grid[0])

        # visited = set()
        # max_area = 0
        # direction = [(1,0), (-1,0), (0,1), (0,-1)]

        # def bfs(r,c):
        #     area = 0
        #     queue = deque()
        #     visited.add((r,c))
        #     queue.append((r,c))

        #     while queue:
        #         row, col = queue.popleft()
        #         area += 1  # Increment area for the current cell
        #         for dr, dc in direction:
        #             ndr = dr + row
        #             ndc = dc + col
                    
        #             if 0 <= ndr < rows and 0 <= ndc < cols and (ndr, ndc) not in visited and grid[ndr][ndc] == 1:
        #                 queue.append((ndr, ndc))
        #                 visited.add((ndr, ndc))
                    
        #     return area

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1 and (r,c) not in visited:
        #             max_area = max(bfs(r,c), max_area)
        
        # return max_area

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        max_area = 0
        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(r,c):
            area = 0
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))

            while queue:
                area+=1
                row, col = queue.popleft()
                for dr, dc in direction:
                    ndr = dr+row
                    ndc = dc+col
                    
                    if 0 <= ndr < rows and 0 <= ndc < cols and (ndr, ndc) not in visited and grid[ndr][ndc] == 1:
                        queue.append((ndr, ndc))
                        visited.add((ndr, ndc))
                    
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(bfs(r,c), max_area)
                    
        
        return max_area