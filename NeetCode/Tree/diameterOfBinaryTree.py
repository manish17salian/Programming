# Question: https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        count = [0]
        def traverse(node):
            if not node:
                return 0
            leftNode = traverse(node.left)
            rightNode = traverse(node.right)

            height = leftNode + rightNode
            count[0] = max(count[0], height)
            return max(leftNode, rightNode)+1
        traverse(root)
        return count[0]