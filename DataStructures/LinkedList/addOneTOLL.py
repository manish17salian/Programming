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
    carry = 0    
    while rnode:
        if count == 0:
            rnode.data+=1
        else: 
            rnode.data += carry
            carry = 0
        
        if rnode.data > 9 and (count == 0 or carry==1):
            rnode.data = 0
            carry = 1

        rnode = rnode.next
        count +=1
    return rnode       
                
    
        

        



