# Question: https://leetcode.com/problems/generate-parentheses/description/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def recurssion(opToken, clToken):
            if opToken == clToken == n:
                res.append("".join(stack))
                return
            
            if opToken < n:
                stack.append("(")
                recurssion(opToken+1, clToken)
                stack.pop()
            
            if clToken < opToken:
                stack.append(")")
                recurssion(opToken, clToken+1)
                stack.pop()
        recurssion(0,0)
        return res               
        