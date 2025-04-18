# Question: https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_found = 0

        for index, val in enumerate(nums):
            if val != 0:
                nums[index], nums[zero_found] = nums[zero_found], nums[index]
                zero_found+=1
        
        return nums
