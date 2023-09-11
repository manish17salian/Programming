# Question: https://www.codingninjas.com/studio/problems/reverse-a-doubly-linked-list_1116098

'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''

def reverseDLL(head):
    # Write your code here
    current = head
    prevNode = None
    while current:
        current.prev, current.next = current.next, current.prev
        prevNode = current
        current = current.prev
    return prevNode
    