# Question: https://www.codingninjas.com/studio/problems/introduction-to-doubly-linked-list_8160413?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1

class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def constructDLL(arr: [int]) -> Node:
    temp = Node(arr[0])
    if len(arr) == 0:
        return None
    current = temp
    for i in range(1, len(arr)):
        new_node = Node(arr[i], prev=current)  # Set the new node's previous pointer to the current node
        current.next = new_node
        current = new_node
    return temp
