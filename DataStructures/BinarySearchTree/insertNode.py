# Question: https://www.codingninjas.com/studio/problems/insert-into-a-binary-search-tree_1279913?leftPanelTabValue=SUBMISSION

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from typing import List

def insertionInBST(root,val):
    if root is None:
        return TreeNode(val)
    current = root
    while True:
        if current.val > val:
            if current.left == None:
                current.left = TreeNode(val)
                break
            else:
                current = current.left
        else:
            if current.right == None:
                current.right = TreeNode(val)
                break
            else:
                current = current.right
    
    return root

        
        