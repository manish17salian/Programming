# Question: https://www.codingninjas.com/studio/problems/trapping-rain-water_630519?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION


from typing import List

def getTrappedWater(arr: List[int], n: int) -> int:
    left_stack = []
    left_stack.append(arr[0])
    right_stack = []
    right_stack.append(arr[-1])
    leftMax = arr[0]
    rightMax = arr[-1]
    def putintoStack(stack, array):
        for i in range(1, len(array)):
            if stack[-1] > array[i]:
                stack.append(stack[-1])         
            else:
                stack.append(array[i])
    putintoStack(left_stack, arr)
    putintoStack(right_stack, arr[::-1])
    right_stack = right_stack[::-1]
    sum = 0
    for i in range(0, len(arr)):
        # if arr[i] != min(left_stack[i], right_stack[i]) :
        sum += abs(arr[i] - min(left_stack[i], right_stack[i]))
    
    return sum
