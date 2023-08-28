# Question: https://www.codingninjas.com/studio/problems/segregate-even-and-odd-nodes-in-a-linked-list_1116100?leftPanelTab=1


'''
Following is the structure of the Node class already defined:
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def segregateEvenOdd(head):
    # Write your code here
    
    if head == None:
        return None
    even_head = None
    even_tail = None
    odd_head = None
    odd_tail = None

    current = head
    while current:
        newNode = Node(current.data)
        if current.data%2 == 0:
            if even_head == None:
                even_head = newNode
                even_tail = even_head
            else:
                even_tail.next = newNode
                even_tail = even_tail.next
        else:
            if odd_head == None:
                odd_head = newNode
                odd_tail = odd_head
            else:
                odd_tail.next = newNode
                odd_tail = odd_tail.next
        current = current.next
    
    if even_head == None:
        return odd_head
    else:
        even_tail.next = odd_head
        return even_head
    
    
    
        

