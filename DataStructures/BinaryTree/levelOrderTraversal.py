# Question: https://www.codingninjas.com/studio/problems/zigzag-binary-tree-traversal_920532?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
# Also called ZIGZAG Traversal
'''
    Following is the structure of Tree Node

    class TreeNode:

        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
'''
from typing import List

def levelOrder(root) -> List[int]:
    if root == None:
        return []
    
    result =[]
    queue = [root]

    while queue:
        popedVal = queue.pop(0)
        result.append(popedVal.data)

        if popedVal.left:
            queue.append(popedVal.left)

        if popedVal.right:
            queue.append(popedVal.right)
    
    return result

        
	
        