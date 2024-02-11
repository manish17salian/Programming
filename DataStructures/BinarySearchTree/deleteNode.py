# Question: https://www.codingninjas.com/studio/problems/delete-node-in-bst_920381?leftPanelTabValue=SUBMISSION
# Solution video: https://www.youtube.com/watch?v=LFzAoJJt92M

# Following is the class structure of the Node class:
class   TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def deleteNode(root, key):
    if root is None:
        return None

    if root.data > key:
        root.left = deleteNode(root.left, key)
    elif root.data < key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            curr = root.right
            while curr.left:
                curr = curr.left
            root.data = curr.data
            root.right = deleteNode(root.right, curr.data)

    return root