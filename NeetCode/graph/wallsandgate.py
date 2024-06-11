# Question: https://neetcode.io/problems/islands-and-treasure

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Initialize the queue with all gates (0's) and set their distances to 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))  # (row, column, distance)

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in direction:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > dist + 1:
                    grid[nr][nc] = dist + 1
                    queue.append((nr, nc, dist + 1))