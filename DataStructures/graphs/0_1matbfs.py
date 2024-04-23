# Question: https://www.naukri.com/code360/problems/distance-of-nearest-cell-having-1-in-a-binary-matrix_1169913?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

from collections import deque
def nearest(mat,n,m):
    row = len(mat)
    col = len(mat[0])
    direction = [(1,0),(-1,0),(0,1), (0,-1)]
    queue = deque()

    dist =[[float('inf')] * m for _ in range(n)]

    for r in range(row):
        for c in range(col):
            if mat[r][c] == 1:
                dist[r][c] = 0
                queue.append((r,c))
    
    while queue:
        r,c = queue.popleft()
        for dr,dc in direction:
            ndr, ndc = r+dr, c+dc
            if 0 <= ndr < row and 0 <= ndc < col and dist[ndr][ndc] == float('inf'):
                dist[ndr][ndc] = dist[r][c]+1
                queue.append((ndr, ndc))
    
    return dist
                
