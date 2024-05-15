# Question: https://www.codingninjas.com/studio/problems/sort-stack_1229505?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION
# Watch: https://www.youtube.com/watch?v=XNAv8NrAwng

from os import *
from sys import *
from collections import *
from math import *

# S is a list of integers

def sortStack(s):
    if not s or len(s) == 1:
        return s
    
    topElement = s.pop()
    sortStack(s)
    recursiveInsert(s, topElement)
    return s

def recursiveInsert(s, topElement):
    if not s or s[-1] < topElement:
        s.append(topElement)
        return
    else:
        print(s, topElement)
        top = s.pop()
        print(s, 'After Pop')
        recursiveInsert(s, topElement)
        s.append(top)
