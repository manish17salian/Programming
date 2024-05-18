# Question: https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(node, level):
            if not node:
                return
            
            if level == len(res):
                res.append(node.val)
            traverse(node.right, level + 1)
            traverse(node.left, level + 1)

        traverse(root, 0)
        return res
        