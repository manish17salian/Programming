# Question: https://www.codingninjas.com/studio/problems/postfix-to-prefix_1788455?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

def postfixToPrefix(s: str) -> str:
    stack = []
    for i in s:
        if i.isalnum():
            stack.append(i)
        else:
            op1 =stack.pop() 
            op2 = stack.pop() 
            intres = i + op2 + op1
            stack.append(intres)

    return stack[0] 