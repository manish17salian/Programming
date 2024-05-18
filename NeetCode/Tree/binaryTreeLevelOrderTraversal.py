# Question: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def traverse(root, res, lvl):
            if root is None:
                return

            if len(res) == lvl:
                res.append([])
            
            res[lvl].append(root.val)
            traverse(root.left, res, lvl+1)
            traverse(root.right, res, lvl+1)
        traverse(root, res,0)
        return res
        