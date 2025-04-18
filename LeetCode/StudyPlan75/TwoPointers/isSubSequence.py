# Question: https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPointer, tPointer = 0, 0
        
        while sPointer < len(s) and tPointer < len(t):
            if s[sPointer] == t[tPointer]:
                sPointer += 1
            tPointer += 1
        
        return sPointer == len(s)

        