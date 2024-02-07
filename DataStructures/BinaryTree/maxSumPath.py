# Question: https://www.codingninjas.com/studio/problems/maximum-sum-path-of-a-binary-tree._1214968?leftPanelTabValue=SOLUTION

# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxPathSum(root: BinaryTreeNode) -> int:
    maxSum = [float('-inf')]
    def traverse(node):
        if node is None:
            return 0
        
        left_node = max(traverse(node.left),0)
        right_node = max(traverse(node.right), 0)
        summation = left_node+right_node+node.data
        maxSum[0] = max(summation, maxSum[0])
        return node.data + max(left_node, right_node)

    traverse(root)
    return maxSum[0]