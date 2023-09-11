# Question: https://www.codingninjas.com/studio/problems/rotate-linked-list_920454?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1


class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next


def rotate(head: Node, k: int) -> Node:
    # Write your code here.
    current = head
    length = 0

    while current:
        current = current.next
        length+=1

    while k>length:
        k = k - length
        # print(k)
    
    if k == length or k == 0:
        return head
    # print(k, '--')
    loop = head
    loop_head = None
    count = 0
    node = None
    node_head = None
    tail = None
    while loop:
        if loop_head == None:
            loop_head = loop
        if count + 1 == length - k:
            node = loop.next
            loop.next = None
            while node:
                if node_head == None:
                    node_head = node
                if node.next == None:
                    node.next = loop_head
                    break;
                node = node.next
            break;
        
        count+=1
        loop = loop.next

    return node_head 


        