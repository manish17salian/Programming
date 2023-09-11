# Question: 'https://www.codingninjas.com/studio/problems/find-pairs-with-given-sum-in-doubly-linked-list_1164172?leftPanelTab=1'

class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def findPairs(head: Node, k: int) -> [[int]]:

    left = head
    current = head
    revNode = None
    rightCount = 0
    while current:
        current.prev, current.next = current.next, current.prev
        revNode = current
        current = current.prev
        rightCount+=1
    right = revNode
    leftCount = 0
    retArr = []
    rightCount-=1

 
    while left and right and leftCount < rightCount:
        summation = left.data + right.data
        if summation == k:
            
            leftCount+=1
            rightCount-=1
            retArr.append((left.data, right.data))
            left = left.prev
            right = right.next
           
        elif summation > k:
            rightCount-=1
            right = right.next
        else:
            leftCount+=1
            left = left.prev

    # print(retArr)
    return retArr  