class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:
    # Write your code here
    def __init__(self):
    # Write your code here
        self.head = None
        
    def getSize(self):
        count = 0
        current = self.head
        while current.next:
            count +=1
            current = current.next
        return count

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def push(self, data):
        current = self.head
        while current.next:
            current = current.next
        current.next = data

    def pop(self):
        if self.head is not None:
            length =  self.getSize()
            current = self.head
            while length is not 1:
                current = current.next
                length -= 1
            current.next = None

    def getTop(self):
        if self.head is not None:
            length =  self.getSize()
            current = self.head
            while length is not 1:
                current = current.next
                length -= 1
            return current.next.data
        else:
            return -1