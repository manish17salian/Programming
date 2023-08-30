# Question: https://www.codingninjas.com/studio/problems/add-one-to-a-number-represented-as-linked-list_920557?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addOne(head: Node) -> Node:
    # write your code here
    while head == None:
        return None
    current = head
    rnode = None
    while current:
        next_node = current.next
        current.next = rnode
        rnode = current
        current = next_node
    count = 0
    carry = 1
    rhead = rnode
    while rhead:
        rhead.data += carry
        if rhead.data > 9 and (rhead.next == None):
            rhead.data = 0
            rhead.next = Node(1)
        if rhead.data > 9 and (carry==1):
            rhead.data = 0
            carry = 1
        else:
            carry = 0

            # carry = 1
        rhead = rhead.next
        count +=1
    current = rnode
    node = None
    while current:
        next_node = current.next
        current.next = node
        node = current
        current = next_node
    
    return node       
                
    
        

        



