# Question: https://www.codingninjas.com/studio/problems/boundary-traversal-of-binary-tree_790725?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# Functions to traverse on each part.
def traverseBoundary(root):
    def checkLeafNode(node):
        if node.left is None and node.right==None:
            return True
        else:
            return False
    
    stack = []
    
    # This block is used to find the left boundry till the leaf node
    def leftNodes(node):    
        curr = node.left
        while curr:
            if not checkLeafNode(curr):
                stack.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right


    # This block is used to find the right boundry till the leaf node.
    # A stack is used so that we ccan give an inverse of the flow
    def rightNode(node):
        curr = node.right
        temp = []
        while curr:
            if not checkLeafNode(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        
        while temp:
            stack.append(temp.pop())

    # Add the leaf node 
    def addLeaf(node):
        if checkLeafNode(node):
            stack.append(node.data)
            return
        # 
        if node.left is not None :
            addLeaf(node.left)
        if node.right is not None:
            addLeaf(node.right)
    
    #Generate the results
    def returnres(node):
        if checkLeafNode(node):
            stack.append(node.data)
            return
        stack.append(node.data)
        leftNodes(node)
        addLeaf(node)
        rightNode(node)

    returnres(root)
    return stack

