# Question: https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for num in nums:
        if (num-1) not in numSet:
            length = 0
            while num+length in numSet:
                length+=1
            longest = max(longest, length)
    return longest
