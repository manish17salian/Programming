# Question: https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursion(left, right):
            if left > right:
                return -1
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                return recursion(mid+1, right)
            else:
                return recursion(left, mid-1)
            
        return recursion(0, len(nums)-1)    
            
        