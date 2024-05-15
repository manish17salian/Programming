
# Question: https://www.codingninjas.com/studio/problems/size-of-largest-bst-in-binary-tree_893103?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION
#Important
from math import inf
'''

    ------- Binary Tree node structure -------
            class TreeNode :
                def __init__(self, data) :
                    self.data = data
                    self.left = None
                    self.right = None

'''

class Node:
    def __init__(self, minVal, maxVal, size):
        self.minVal = minVal
        self.maxVal = maxVal
        self.size = size

def largestBST(root):

    def traversal(node):
        if node is None:
            return Node(inf, -inf, 0)
        left_node = traversal(node.left)
        right_node = traversal(node.right)

        if left_node.maxVal < node.data < right_node.minVal:
            return Node(min(node.data, left_node.minVal), max(node.data, right_node.maxVal), left_node.size + right_node.size + 1)

        return Node(-inf, inf,max(left_node.size, right_node.size))
    
    return traversal(root).size
        