# Question: https://www.codingninjas.com/studio/problems/height-of-binary-tree_4609628?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    stack = [(root, 1)]
    max_depth = 0

    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))

    return max_depth

def maxDepth(root: TreeNode) -> int:
    def traverse(node):
        if node is None:
            return 0
        left_depth = traverse(node.left)
        right_depth = traverse(node.right)
        return max(left_depth, right_depth) + 1
    
    return traverse(root)