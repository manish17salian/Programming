# Question: LeetCode: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)
        for i in range(1,len(preorder)):
            node = TreeNode(preorder[i])
            if node.val < stack[-1].val:
                stack[-1].left = node
            else:
            
                while stack and stack[-1].val < node.val:
                    l = stack.pop()
                l.right = node
            stack.append(node)
        return root