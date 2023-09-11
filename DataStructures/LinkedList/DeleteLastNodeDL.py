# Question: https://www.codingninjas.com/studio/problems/delete-last-node-of-a-doubly-linked-list_8160469?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Do not change code above.


def deleteLastNode(head: Node) -> Node:
    # Write your code here
    current = head
    if head == None:
        return None
    while current.next:
        current = current.next
    else:
        if current.prev:
            current = current.prev
            current.next = None
        else:
            return None
                
    return head
