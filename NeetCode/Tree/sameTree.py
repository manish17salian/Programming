# Question: https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if (root1 is None) and (root2 is None):
            return True
    
        if (root1 is None) or (root2 is None):
            return False
        return (root1.val == root2.val) and self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)