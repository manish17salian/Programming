# Question: https://www.codingninjas.com/studio/problems/capacity-to-ship-packages-within-d-days_1229379?leftPanelTabValue=SUBMISSION


from os import *
from sys import *
from collections import *
from math import *

def leastWeightCapacity(weights, d):
    if d == 1:
        return sum(weights)
    def checkCapacity(val):
        capacity = 0
        day = 1
        for i in weights:
            if capacity+i <= val:
                capacity+=i
            else:
                day+=1
                capacity = i
        
        return day

            
    def binary(left, right):
        if left > right:
            return left
        mid = (left+right)//2
        val = checkCapacity(mid)
        if val <= d:
            return binary(left, mid-1)
        else:
            return binary(mid+1, right)
    return binary(max(weights), sum(weights))
