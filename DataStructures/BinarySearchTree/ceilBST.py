# Question: https://www.codingninjas.com/studio/problems/ceil-from-bst_920464?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def findCeil(root, x):
    # stack = []
    # def traversal(node):
    #     if node is None:
    #         return
    #     traversal(node.left)
    #     stack.append(node.data)
    #     traversal(node.right)
    # traversal(root)
    # minVal = -1
    # while stack:
    #     value = stack.pop()
    #     if value >= x:
    #         minVal = value
    #     else:
    #         break
    
    # return minVal


    ceil = -1

    while root:
        if root.data == x:
            return root.data
        
        if root.data > x:
            ceil = root.data
            root = root.left
        else:
            root = root.right

    
    return ceil
        