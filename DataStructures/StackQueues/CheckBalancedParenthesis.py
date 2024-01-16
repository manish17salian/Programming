#Question: https://www.codingninjas.com/studio/problems/valid-parentheses_795104?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION


from collections import deque

def isValidParenthesis(s: str) -> bool:
    brackets = {
        '(':')',
        '{':'}',
        '[':']'
    }
    stack = deque()
    for i in s:
        if i in brackets.values():
            if len(stack) == 0  or i != brackets[stack[-1]]:
                return False
            else:
                stack.pop()
        elif i in brackets.keys():
            stack.append(i)
        else:
            return False

    return not stack
            