# Question: https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackT, stackI = stack.pop()
                res[stackI] = abs(stackI - index)
            stack.append((temp, index))
        return res


