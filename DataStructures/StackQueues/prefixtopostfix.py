# Question: https://www.codingninjas.com/studio/problems/convert-prefix-to-postfix_8391014?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION


from typing import List

def preToPost(s: str) -> str:
    s = s[::-1]
    stack = []
    for i in s:
        if i.isalnum():
            stack.append(i)
        else:
            op1 = stack.pop()   
            op2 = stack.pop() 
            intRes = op1 + op2 + i
            stack.append(intRes)
    
    return ''.join(stack)