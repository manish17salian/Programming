# Question:https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for index, num in enumerate(nums):
            rest = target - num
            if rest in numToIndex:
                return [numToIndex[rest], index]
            numToIndex[num] = index
        