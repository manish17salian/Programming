# Question: https://www.codingninjas.com/studio/problems/clone-a-linked-list-with-random-pointers_983604?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

class Node:
    def __init__(self, data=0, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random


# Don't change the code above.


def cloneLL(head: Node) -> Node:
    while head == None:
        return head
    
    current = head
    while current:
        newNode = Node(current.data)
        newNode.next = current.next
        current.next = newNode
        current = newNode.next

    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    
    current = head
    newHead = head.next
    newCurrent = newHead

    while current:
        current.next = newCurrent.next
        current = current.next
        if current:
            newCurrent.next = current.next
            newCurrent = newCurrent.next

    return newHead




    

