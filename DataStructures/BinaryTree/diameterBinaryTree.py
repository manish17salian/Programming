# Question: https://www.codingninjas.com/studio/problems/diameter-of-binary-tree_920552?leftPanelTabValue=SUBMISSION


# Following is the TreeNode class structure.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diameterOfBinaryTree(root: TreeNode) -> int:
    # 'count' is a list used to keep track of the maximum diameter found so far.
    # We use a list here instead of an integer so that 'count' can be updated within 'traverse'
    # and the updated value persists outside of the function's scope.
    count = [0]

    # This nested function 'traverse' calculates the height of the tree rooted at 'node',
    # and updates the 'count' with the diameter at 'node'.
    def traverse(node):
        # Base case: if the current node is None, the height is 0.
        if node is None:
            return 0
        
        # Recursively find the height of the left subtree.
        left_height = traverse(node.left)
        # Recursively find the height of the right subtree.
        right_height = traverse(node.right)
        
        # The 'height' at 'node' is the sum of heights of the left and right subtrees.
        # This is part of the diameter if 'node' is used as the connecting path.
        height = left_height + right_height
        
        # Update the 'count' with the larger value between the current 'height' and the previous 'count'.
        count[0] = max(height, count[0])
        
        # Return the height of the tree rooted at 'node', which is the max height of its subtrees plus 1 for 'node' itself.
        return max(left_height, right_height) + 1
    
    # Call the 'traverse' function starting from the 'root'.
    # This will update 'count' to have the maximum diameter.
    traverse(root)
    
    # Return the maximum diameter found during the traversal.
    return count[0]

# Example usage:
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# print(diameterOfBinaryTree(root))  # Should print the diameter of the binary tree



#Similar to finding height of the tree
