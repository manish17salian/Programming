# Question:'https://www.codingninjas.com/studio/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list_8160461?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf'

class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def deleteAllOccurrences(head: Node, k: int) -> Node:
    
    current = head
    prev = None

    while current:
        if current.data == k:
            if prev:
                prev.next = current.next
                if current.next:
                    current.next.prev = prev
            else:
                head = current.next
                if current.next:
                    current.next.prev = None
        else:
            prev = current
        current = current.next

    return head