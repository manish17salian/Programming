# Question: https://leetcode.com/problems/non-overlapping-intervals/


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda x:x[0])
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                res+=1
                prevEnd = min(intervals[i][1], prevEnd)
        return res 