# Question: https://www.naukri.com/code360/problems/rotting-oranges_701655?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from collections import deque
def minTimeToRot(grid, n, m):
    row = len(grid)
    col = len(grid[0])
    fresh = 0
    time = 0
    queue = deque()

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 2:
                queue.append((r,c,0))
            elif grid[r][c] == 1:
                fresh+=1
    
    direction = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c, currTime = queue.popleft()
        time = max(currTime, time)

        for dr, dc in direction:
            nr = r+dr
            nc = c+dc

            if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                queue.append((nr,nc, currTime+1))
                fresh-=1
    

    if fresh > 0:
        return -1
    else:
        return time