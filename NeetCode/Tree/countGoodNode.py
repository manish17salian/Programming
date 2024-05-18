# Question: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def traverse(root, arr, maxVal):
            if not root:
                return res[0]
            if root.val >= maxVal:
                res[0]+=1
            
            maxVal = max(maxVal, root.val)
            arr.append(root.val)
            traverse(root.left, res, maxVal)
            traverse(root.right, res, maxVal)
        
        traverse(root, res, root.val)
        return res[0]

        