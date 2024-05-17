# Question: https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = 0
        left = 0
        mapDict = {}
        for right, val in enumerate(s):
            if val in mapDict:
                mapDict[val] +=1
            else:
                mapDict[val] = 1
            
            count = max(count, mapDict[val])
            if (right-left+1) - count > k:
                mapDict[s[left]]-=1
                left+=1
            res = max(res, right-left+1)
        return res
        