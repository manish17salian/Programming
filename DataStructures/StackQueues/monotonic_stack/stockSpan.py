# Question: https://www.codingninjas.com/studio/problems/stock-span_5243295?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION


from typing import List

def findStockSpans(prices: List[int]) -> List[int]:
    n = len(prices)
    span = [1]*n
    stack = []
    for i, num in enumerate(prices):
        while stack and prices[stack[-1]] < num:
            stack.pop()
        
        if stack:
            span[i] = i - stack[-1]
        else:
            span[i] = i + 1
        
        stack.append(i)
    return span