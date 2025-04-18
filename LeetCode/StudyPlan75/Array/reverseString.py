# Question: https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        pushStr = ""
        for i in s:
            if i == " " and pushStr == "":
                continue
            if i == " ":
                stack.append(pushStr)
                pushStr = ""
            else:
                pushStr+=i
        if pushStr:
            stack.append(pushStr)
        print(stack)
        res = ""
        while stack:
            res+=stack.pop()
            if stack:
                res+= " "
        return res