# qUESTION: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:

        def recurssion(left, right):
            if left == right:
                return nums[left]
            
            mid = left+(right-left)//2
            if nums[left] < nums[right]:
                return nums[left]
            if nums[mid] >= nums[left]:
                return recurssion(mid+1, right)
            else:
                return recurssion(left, mid)
        return recurssion(0, len(nums)-1)
        