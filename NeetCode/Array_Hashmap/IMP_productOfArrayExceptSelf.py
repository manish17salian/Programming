# Question: https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = 1
        results = [1]*len(nums)

        for i in range(1,len(nums)):
            results[i] = results[i-1]*nums[i-1]

        for i in range(len(nums)-1,-1,-1):
            results[i]*=postfix
            postfix*=nums[i] 
        return results     
