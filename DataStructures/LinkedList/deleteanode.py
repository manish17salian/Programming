# Question: https://practice.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=delete-a-node-in-single-linked-list

class node:
    def __init__(self):
        self.data = None
        self.next = None


def delNode(head, k):
    # Code here
    temp = node()
    if head is None:
        return temp
    ind = 1
    current = head
    prev = None

    while current:
        if ind == k:
            prev.next = current.next
            return head
        else:
            prev = current
            current = current.next
            ind += 1
    
    return head