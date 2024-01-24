# Question: https://www.codingninjas.com/studio/problems/postfix-to-infix_8382386?leftPanelTabValue=SUBMISSION


def postToInfix(postfix: str) -> str:
    stack = []
    for i in postfix:
        if i.isalnum():
            stack.append(i)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            infix_result = '({}{}{})'.format(op2, i, op1)
            stack.append(infix_result)

    return stack[0]