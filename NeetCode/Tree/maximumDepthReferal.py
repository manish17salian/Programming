# Question: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        def recurssion(root):
            if not root:
                return 0
            
            leftDept = recurssion(root.left)
            rightDept = recurssion(root.right)
            return max(leftDept, rightDept) + 1
        
        return recurssion(root)

        