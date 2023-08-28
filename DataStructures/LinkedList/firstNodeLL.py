# Question: https://www.codingninjas.com/studio/problems/linked-list-cycle-ii_1112628?leftPanelTab=2

'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def firstNode(head):
    # Write your code here
    if head == None:
        return None
    current = head
    temp = set()
    while current is not None:
        if current in temp:
            return current
        else:
            temp.add(current)

        current = current.next
        
    return None