# Question: https://www.codingninjas.com/studio/problems/cycle-detection-in-a-singly-linked-list_628974?leftPanelTab=2


'''
Following is the structure of the Node class already defined.

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
'''

def detectCycle(head) :
    # Write your code here.
    visited = set()
    current = head

    while current is not None:
        if current in visited:
            return True
        visited.add(current)
        current = current.next

    return False
    