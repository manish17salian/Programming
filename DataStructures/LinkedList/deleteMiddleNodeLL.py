# Question: https://www.codingninjas.com/studio/problems/delete-middle-node_763267?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


'''
Following is the structure of the Node class already defined:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def deleteMiddle(head):
    # Write your code here.
    length = 0
    while head == None:
        return head

    
    current = head
    start = head
    while current:
        length+=1
        current = current.next
    
    if length == 1:
        return None
    
    middle = 0
    if length%2==0:
        middle = length//2
    else:
        middle = (length//2)
    
    count = 0
    prev = None
    while start:
        if count == middle:
            prev.next = start.next
        else:
            prev = start
        start = start.next
        count+=1
    return head