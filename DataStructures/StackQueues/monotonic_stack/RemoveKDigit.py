# Question: https://www.codingninjas.com/studio/problems/remove-k-digits_1461221?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

def removeKDigits(num, k):
    stack = []
    for i in num:
        while stack and k>0 and stack[-1] > i:
            stack.pop()
            k-=1
        stack.append(i)
    
    if k>0:
        stack = stack[:-k]
    return "".join(stack).lstrip("0") or "0"