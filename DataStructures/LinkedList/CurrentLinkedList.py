# Question: https://www.codingninjas.com/studio/problems/search-in-a-linked-list_975381?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0


'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def searchInLinkedList(head, k):
    current = head
    if current == None:
        return 0
    con = 0
    while current:
        if current.data == k:
            con = 1
            break;
        else:
            current = current.next
    return con