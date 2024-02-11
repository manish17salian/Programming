# Question: https://www.codingninjas.com/studio/problems/kth-smallest-node-in-bst_920441?leftPanelTabValue=SUBMISSION

from typing import Optional

class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    elements = []
    def traversal(node):
        if node is None:
            return
        traversal(node.left)
        elements.append(node.data)
        traversal(node.right)
    traversal(root)
    if 0 < k <= len(elements):
        return elements[k - 1]
    else:
        return -1
