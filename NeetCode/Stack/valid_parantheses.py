# Question: https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        parDict = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        
        stack = []
        for i in range(len(s)):
            if s[i] in parDict:
                if stack and parDict[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return not stack
