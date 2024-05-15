# Question: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers)-1
        while pointer1 < pointer2:
            if numbers[pointer2] + numbers[pointer1] > target:
                pointer2-=1
            elif numbers[pointer2] + numbers[pointer1] < target:
                pointer1+=1
            else:
                return [pointer1+1, pointer2+1]

        