# Question: https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        longestString = ""
        longestCount = 0
        for index, i in enumerate(s):
            # if len(s)%2 == 0:
            #     l,r = index,index+1
            # else:
            #     l,r = index, index
            l,r = index,index
            while (l >= 0 and r < len(s)) and (s[l] == s[r]):
                if r-l+1 > longestCount:
                    longestString = s[l:r+1]
                    longestCount = max(longestCount, r-l+1)
                l-=1
                r+=1
            
            l,r = index, index+1
            while (l >= 0 and r < len(s)) and (s[l] == s[r]):
                if r-l+1 > longestCount:
                    longestString = s[l:r+1]
                    longestCount = max(longestCount, r-l+1)
                l-=1
                r+=1
        if longestString != "":
            return longestString
        else:
            return s[0]
