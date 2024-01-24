# Question: https://www.codingninjas.com/studio/problems/prefix-to-infix_1215000?leftPanelTabValue=SUBMISSION


def prefixToInfixConversion(s: str) -> str:
    s = s[::-1]
    stack = []
    for i in s:
        if i.isalnum():
            stack.append(i)
        else:
            op1 = stack.pop()   
            op2 = stack.pop() 
            intRes = '(' + op1 + i + op2 + ')'
            stack.append(intRes)
    
    return ''.join(stack)