# Question: https://www.codingninjas.com/studio/problems/sum-of-subarray-minimums_8365431?leftPanelTabValue=SUBMISSION

from typing import *
from collections import *

def sumSubarrayMins(N:int, arr:List[int]) -> int:
    leng = len(arr)
    left_stack = [-1 for i in range(len(arr))]
    right_stack = [len(arr) for i in range(len(arr))]
    stack = []
    for i in range(leng-1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            right_stack[i] = stack[-1]
        
        stack.append(i)

    stack = []
    
    for i in range(leng):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left_stack[i] = stack[-1]
        stack.append(i)
    mod = 10**9 + 7
    result = sum((i - left_stack[i]) * (right_stack[i] - i) * value for i, value in enumerate(arr)) % mod
    return result 