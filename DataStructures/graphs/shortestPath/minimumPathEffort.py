# Question: https://leetcode.com/problems/path-with-minimum-effort/


from collections import deque
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        heap = []
        heapq.heappush(heap, (0, 0, 0))
        distList = [[float("inf")]*col for _ in range(row)]
        distList[0][0] = 0
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        while heap:
            dist, r, c = heapq.heappop(heap)
            if row-1 == r and col-1 == c:
                return dist
            for dr, dc in direction:
                ndr = dr+r
                ndc = dc+c
                if 0<=ndr<row and 0<=ndc<col:
                    effort = max(abs(heights[r][c] - heights[ndr][ndc]), dist)
                    if effort < distList[ndr][ndc]:
                        distList[ndr][ndc] = effort
                        heapq.heappush(heap, (effort, ndr, ndc))
        
        return -1

            

