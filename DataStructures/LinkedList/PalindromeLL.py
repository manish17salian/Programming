# Question: https://www.codingninjas.com/studio/problems/check-if-linked-list-is-palindrome_985248

'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def isPalindrome(head):
    # write your code here
    if head == None:
        return None
    current = head
    temp = []
    while current:
        temp.append(current.data)
        current = current.next
    left = 0
    right = len(temp)-1
    while left < right:
        if temp[left] != temp[right]:
            return False
        left += 1
        right -= 1
    
    return True