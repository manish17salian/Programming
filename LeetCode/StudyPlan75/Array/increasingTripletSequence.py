# Question: https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = float("inf")
        mid = float("inf")

        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            else:
                return True
        
        return False
        