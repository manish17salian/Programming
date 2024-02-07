# Question: https://www.codingninjas.com/studio/problems/create-binary-tree_8360671?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from typing import List

class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def createTree(arr: List[int], index=0) -> Node:
    if index < len(arr):
        root = Node(arr[index])

        root.left = createTree(arr, 2*index+1)
        root.right = createTree(arr, 2*index+2)
        return root
    else:
        return None
    
###
    # Recursive function: See Obsidein notes for explanation
###