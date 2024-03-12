# Question: https://www.codingninjas.com/studio/problems/floor-from-bst_625868?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

def floor(root, x):
    if root is None:
        return
    floor = -1
    while root:
        if root.data == x:
            return root.data
        if root.data < x:
            floor = root.data
            root = root.right
           
        else:
            root = root.left

    return floor