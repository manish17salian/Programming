# Question: https://www.codingninjas.com/studio/problems/count-nodes-of-linked-list_5884?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def length(head) :
    # temp=Node()
    current = head
    if current == None:
        return 0
    
    count = 1
    while current.next:
        if current == -1:
            return count
        else:
            count+=1
            current = current.next
    return count