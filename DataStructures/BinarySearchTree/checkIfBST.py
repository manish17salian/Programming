# Question: https://www.codingninjas.com/studio/problems/check-bst_5975?leftPanelTabValue=SUBMISSION
# Intution: CHeck for range


from sys import stdin
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
INT_MIN = -2147483648
INT_MAX = 2147483647


def isBST(root):
    '''
    Given a binary tree with N number of nodes, check if that input tree is
    BST (Binary Search Tree) or not. If yes, return True, return False
    otherwise. Duplicate elements should be in right subtree.

    '''
    # Write your code herea)
    def traversal(node, minVal, maxVal):
        if node is None:
            return True

        if not (minVal < node.data <= maxVal):
            return False

        return traversal(node.left, minVal, node.data-1) and traversal(node.right, node.data, maxVal) 

    return traversal(root, INT_MIN, INT_MAX)








#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root


# Main

root = takeInput()
print('true') if isBST(root) else print('false')