from os import *
from sys import *
from collections import *
from math import *

def sortArray(arr, n):
    left = 0
    mid = 0
    right = n-1

    while mid <= right:
        if arr[mid] == 0:
            arr[mid], arr[left] = arr[left], arr[mid]
            mid += 1
            left += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1
    
    return arr
