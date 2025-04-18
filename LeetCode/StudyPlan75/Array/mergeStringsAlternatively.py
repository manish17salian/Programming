# Question: https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        s = ""
        for i in range(min(len(word1), len(word2))):
            s+=word1[i] + word2[i]
        
        if len(word1) > len(word2):
            s += word1[len(word2):]
        elif len(word1) < len(word2):
            s += word2[len(word1):]
    
        return s
        
        
        