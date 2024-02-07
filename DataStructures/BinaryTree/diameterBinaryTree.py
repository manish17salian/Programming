# Question: https://www.codingninjas.com/studio/problems/diameter-of-binary-tree_920552?leftPanelTabValue=SUBMISSION


# Following is the TreeNode class structure.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diameterOfBinaryTree(root: TreeNode) -> int:
    # Write your code here.
    count = [0]
    def traverse(node):
        if node is None:
            return 0
        
        left_node = traverse(node.left)
        right_node = traverse(node.right)
        height = left_node + right_node
        count[0] = max(height, count[0])
        return max(left_node,right_node) + 1
    
    traverse(root)
    return count[0]


#Similar to finding height of the tree
