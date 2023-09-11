# Question: https://www.codingninjas.com/studio/problems/introduction-to-linked-list_8144737?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf



class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Do not change code above.


def constructLL(arr: [int]) -> Node:
    # Write your code here
    temp = Node(arr[0])
    current = temp
    for i in range(1, len(arr)):
        current.next = Node(arr[i])  # Create a new node with data from arr[i]
        current = current.next
    return temp