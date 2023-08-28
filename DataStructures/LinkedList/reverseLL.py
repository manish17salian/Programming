# Question: https://www.codingninjas.com/studio/problems/reverse-linked-list_920513?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def reverseLinkedList(head):
    # write your code here
    current = head
    prev = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

        
    return prev

