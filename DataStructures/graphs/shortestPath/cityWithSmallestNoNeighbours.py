# Question: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[float("inf")]*(n) for _ in range(n)]

        for i in range(n):
            matrix[i][i] = 0
        
        for u, v, w in edges:
            matrix[u][v] = w
            matrix[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] != float("inf") and  matrix[k][j] != float("inf"):
                        matrix[i][j] = min(matrix[i][k] + matrix[k][j], matrix[i][j])
        

        min_count = float('inf')
        city_result = 0

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and matrix[i][j] <= distanceThreshold:
                    count += 1
            # Step 4: Determine the best city
            if count < min_count or (count == min_count and i > city_result):
                min_count = count
                city_result = i

        return city_result
        