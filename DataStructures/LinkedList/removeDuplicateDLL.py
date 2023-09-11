# Question: https://www.codingninjas.com/studio/problems/remove-duplicates-from-a-sorted-doubly-linked-list_2420283?leftPanelTab=1

class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def removeDuplicates(head: Node) -> Node:
    current = head
    if head == None:
        return None
    
    prev = None
    while current:
        if current.next and current.data == current.next.data:
            current.next = current.next.next  # Remove the duplicate without updating prev
        else:
            current = current.next  # Move to the next node
    return head
