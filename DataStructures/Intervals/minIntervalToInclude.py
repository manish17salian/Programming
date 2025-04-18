# Question: https://leetcode.com/problems/minimum-interval-to-include-each-query/description/


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = {}
        intervals.sort()
        heap = []
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and q >= intervals[i][0]:
                l, r = intervals[i]
                heapq.heappush(heap, (r-l+1, r))
                i+=1
            
            while heap and q > heap[0][1]:
                heapq.heappop(heap)
            res[q] = heap[0][0] if heap else -1
        
        return [res[q] for q in queries]