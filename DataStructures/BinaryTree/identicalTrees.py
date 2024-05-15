# Question: https://www.codingninjas.com/studio/problems/check-identical-trees_799364


# Following is the structure of BinaryTree Node
class BinaryTreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        
def identicalTrees(root1: BinaryTreeNode, root2: BinaryTreeNode) -> bool:
    if (root1 is None) and (root2 is None):
        return True
    
    if (root1 is None) or (root2 is None):
        return False
    return (root1.val == root2.val) and identicalTrees(root1.left, root2.left) and identicalTrees(root1.right, root2.right)