# Question: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def traverse(root, arr):
            if root is None:
                return
            traverse(root.left, arr)
            arr.append(root.val)
            traverse(root.right, arr)
        traverse(root, res)
        return res[k-1] if 0< k <= len(res) else -1
