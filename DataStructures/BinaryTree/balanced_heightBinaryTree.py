# Question: https://www.codingninjas.com/studio/problems/is-height-balanced-binary-tree_975497?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBalancedBT(root: BinaryTreeNode) -> bool:
    
    def traverse(node):
        if node is None:
            return 0, True
        
        left_Node, isLBalanced = traverse(node.left)
        right_Node, isRBalanced = traverse(node.right)
        isBalanced = (isLBalanced and isRBalanced and 
        abs(left_Node-right_Node) <= 1)

        return max(left_Node, right_Node)+1, isBalanced
    
    return traverse(root)[1]
