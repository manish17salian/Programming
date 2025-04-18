# Question: https://leetcode.com/problems/merge-intervals/description/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        stack = []

        for interval in intervals:
            if not stack or stack[-1][1] < interval[0]:
                stack.append(interval)
            else:
                last_interval = stack.pop()
                new_interval = [min(last_interval[0], interval[0]), max(last_interval[1], interval[1])]
                stack.append(new_interval)

        return stack