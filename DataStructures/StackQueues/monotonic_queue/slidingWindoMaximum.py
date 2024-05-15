# Question: https://www.codingninjas.com/studio/problems/sliding-maximum-_701652?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

def maxSlidingWindow(arr, n, k):
    queue = []
    result = []
    for i, num in enumerate(arr):
        while queue and queue[0] < i-k+1:
            queue.pop(0)
        
        while queue and arr[queue[-1]] < num:
            queue.pop()
        
        queue.append(i)

        if i>=k-1:
            result.append(arr[queue[0]])
        
    return result
nums = [1,3,-1,-3,5,3,6,7]
k = 3
result = maxSlidingWindow(nums, k)
print(result)