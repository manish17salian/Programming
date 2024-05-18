# Question: https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(root):
            if not root:
                return 0, True
            leftNode, leftCheck = traverse(root.left)
            rightNode, rightCheck = traverse(root.right)
            height = abs(leftNode - rightNode)
            check = leftCheck and rightCheck and height<=1
            return max(leftNode, rightNode)+1, check
        return traverse(root)[1]
        