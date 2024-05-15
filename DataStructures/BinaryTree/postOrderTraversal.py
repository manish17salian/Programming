# Question: https://www.codingninjas.com/studio/problems/postorder-traversal_2035933?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


'''
    Following is the structure of Tree Node

    class TreeNode:

        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
'''
from typing import List

def postorderTraversal(root, ans=[]) -> List[int]:

    if (root == None):
        return
    postorderTraversal(root.left, ans)
    postorderTraversal(root.right, ans)
    ans.append(root.val)

    return ans



# Using Stacks: 2 stacks required

def postorderTraversal(root, ans=[]) -> List[int]:
    if root == None:
        return
    
    stack1 = []
    stack2 = []
    result = []

    stack1.append(root)
    while stack1:
        popVal = stack1.pop()
        stack2.append(popVal)
        if popVal.left is not None:
            stack1.append(popVal.left)
        if popVal.right is not None:
            stack1.append(popVal.right)

    while stack2:
        result.append(stack2.pop().val)
    return result
