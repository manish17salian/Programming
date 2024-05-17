# Question: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recurssion(left, right):
            if left > right:
                return -1
            mid = left+(right-left)//2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if nums[mid] > target >= nums[left]:
                    return recurssion(left, mid-1)
                else:
                    return recurssion(mid+1, right)
                    
            else:
                if nums[mid] < target <= nums[right]:
                    return recurssion(mid+1, right)
                else:
                    return recurssion(left, mid-1)
        return recurssion(0, len(nums)-1)
        