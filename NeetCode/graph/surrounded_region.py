# Question: https://leetcode.com/problems/surrounded-regions/description/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        region = [[0]*cols for _ in range(rows)]

        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            region[r][c] = 1

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    ndr, ndc = dr+row, dc+col
                    if 0<=ndr< rows and 0<=ndc<cols and  board[ndr][ndc] == "O" and region[ndr][ndc] == 0:
                        region[ndr][ndc] = 1
                        queue.append((ndr, ndc))


        

        for c in range(cols):
            if board[0][c] == 'O' and region[0][c] == 0:
                bfs(0,c)
            
            if board[rows-1][c] == 'O' and region[rows-1][c] == 0:
                bfs(rows-1, c)
            
        for r in range(rows):
            if board[r][0] == 'O' and region[r][0] == 0:
                bfs(r, 0)
        
            if board[r][cols-1] == 'O' and region[r][cols-1] == 0:
                bfs(r, cols-1)
        
        for i in range(rows):
            for j in range(cols):
                if region[i][j] == 0 and board[i][j] == 'O':
                    board[i][j] = 'X'
        
        return region

                