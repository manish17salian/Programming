# Question: https://www.codingninjas.com/studio/problems/generate-all-parenthesis_920445?leftPanelTabValue=SUBMISSION

def validParenthesis(n: int) -> int:
    result = []
    def recursion(current, left, right):
        if len(current) == 2*n:
            result.append(current)
            return
        if left < n:
            recursion(current+'(', left+1, right)
        if right<left:
            recursion(current+')', left, right+1)
    
    recursion('', 0, 0)
    return result
            