# Question: https://practice.geeksforgeeks.org/problems/linked-list-insertion-1587115620/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=linked-list-insertion


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        c = Node(x)
        if head is None:
            return c
        c.next = head
        return c
        
        
        # code here 
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        c = Node(x)
        if head is None:
            return c
        ptr = head
        #we use a pointer to find the last node of list.
        while ptr.next:
            ptr=ptr.next;
        
        ptr.next = c;
        
        #returning the linked list.
        return head
