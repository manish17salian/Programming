# Question: https://leetcode.com/problems/rotting-oranges/submissions/1284213905/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh+=1
                elif grid[row][col] == 2:
                    queue.append((row, col, 0))

        while queue:
            r, c, currTime = queue.popleft()
            time = currTime

            for dr, dc in direction:
                ndr, ndc = dr+r, dc+c
                if 0<=ndr<rows and 0<=ndc<cols and grid[ndr][ndc] == 1:
                    fresh-=1
                    grid[ndr][ndc] = 2
                    queue.append((ndr, ndc, currTime+1))
        if fresh > 0:
            return -1
        else:
            return time

                
        