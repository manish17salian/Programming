# Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringSet = set()
        left = 0
        res = 0
        for index, right in enumerate(s):
            while right in stringSet:
                stringSet.remove(s[left])
                left+=1
            stringSet.add(right)
            res = max(res, index-left+1)
        return res

            
            
