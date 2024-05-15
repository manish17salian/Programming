# Question: https://www.codingninjas.com/studio/problems/maximum-consecutive-ones_892994?leftPanelTabValue=SUBMISSION&customSource=studio_nav


def longestSubSeg(arr, n, k):
    left = 0
    zeroCount = 0
    maxLength = 0

    for right in range(n):
        if arr[right] == 0:
            zeroCount +=1

        while zeroCount > k:
            if arr[left] == 0:
                zeroCount -=1
            left +=1
        
        
        maxLength = max(maxLength, right - left + 1)
            
    return maxLength
        