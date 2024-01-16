#Question: https://www.codingninjas.com/studio/problems/day-23-:-infix-to-postfix-_1382146?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION


def infixToPostfix(exp: str) -> str:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def checkOperator(i):
        return i in precedence
    
    def checkHigherPrecedence(i, j):
        return precedence[i] >= precedence [j]

    output = []
    exp_stack = []
    for i in exp:
        if i.isalnum():
            output.append(i)
        elif i == '(':
            exp_stack.append(i)
        elif i == ')':
            while exp_stack and exp_stack[-1] != '(':
                output.append(exp_stack.pop())
            exp_stack.pop()
        else:
            while exp_stack and exp_stack[-1] != '(' and checkHigherPrecedence(exp_stack[-1], i):
                output.append(exp_stack.pop())
            exp_stack.append(i)
    while exp_stack:
        output.append(exp_stack.pop())

    return ''.join(output)



# [+, (, *, )]