# Question: https://www.codingninjas.com/studio/problems/count-substrings-with-k-ones_3128698?leftPanelTabValue=PROBLEM

from typing import List

def subarrayWithSum(arr: List[int], k: int) -> int:
    left = 0
    count = 0
    res = 0

    for right in range(len(arr)):
        if arr[right] == 1:
            count+=1
        
        while count > k:
            if arr[left] == 1:
                count-=1
            left+=1
        
        if count == k:
            temp = left
            while temp <=right and count == k:
                res+=1
                if arr[temp] == 1:
                    break
                temp+=1
        
    return res
