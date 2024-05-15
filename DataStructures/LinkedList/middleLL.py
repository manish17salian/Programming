# Question: https://www.codingninjas.com/studio/problems/middle-of-linked-list_973250?leftPanelTab=1


from math import *
from collections import *
from sys import *
from os import *

'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''

def findMiddle(head):
    # Write your code here
    # head denoted head of linked list
    node_len = 0
    current = head
    while current.next:
        node_len +=1
        current = current.next
    start = 0
    if node_len%2 == 0:
        start = node_len//2
    else:
        start=(node_len//2)+1
    # print(start)
    count = 0
    newCurrent = head
    while newCurrent:
        if count == start:
            head = newCurrent
        newCurrent = newCurrent.next
        count+=1
        
    return head



# Optimal Approach (Tortise and Hare approach)
    slow = head
    fast = head
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    
    return slow


