# Question: https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxArea = 0
        while left<right:
            area = min(height[left], height[right])*(right-left)
            maxArea = max(maxArea,area)
            if height[left] >= height[right]:
                right-=1
            elif height[left] < height[right]:
                left+=1
        return maxArea

        