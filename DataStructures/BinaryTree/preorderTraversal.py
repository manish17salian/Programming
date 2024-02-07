# Question: https://www.codingninjas.com/studio/problems/preorder-binary-tree_5948?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrder(root):
    values = []
    def traverse(node):
        if node is None:
            return
        values.append(node.data)  
        traverse(node.left)     
        traverse(node.right) 
    traverse(root)
    return values


#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

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
preOrder(root)


# In preorder traversal print the node and go to the left node. Traverse until you find no child node and then go back to first node.