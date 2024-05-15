from os import *
# Question: https://www.codingninjas.com/studio/problems/inorder-traversal_3839605?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from sys import *
from collections import *
from math import *

'''
    Following is the Binary Tree node structure:
    class TreeNode:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''


def getInOrderTraversal(root):
    values = []
    
    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        values.append(node.data)
        traverse(node.right)
    
    traverse(root)
    return values