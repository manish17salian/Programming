
# Question: https://www.codingninjas.com/studio/problems/kth-missing-element_893215?leftPanelTabValue=SUBMISSION

from typing import *
def missingK(vec: List[int], n: int, k: int) -> int:
    # j = 0
    # for i in range(1, max(vec)+1):
    #     if i == vec[j]:
    #         j+=1
    #     else:
    #         k-=1
        
    #     if k == 0:
    #         return i
    # val = max(vec)
    # while k != 0:
    #     val+=1
    #     k-=1
    # return val
    def binary(left, right):
        if left > right:
            return k+right+1
        mid = (left+right)//2
        val = vec[mid] - (mid+1)
        if val >= k:
            return binary(left, mid-1)
        else:
            return binary(mid+1, right)
    return binary(0, n-1)