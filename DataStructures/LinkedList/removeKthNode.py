# Question: https://www.codingninjas.com/studio/problems/delete-kth-node-from-end_799912?leftPanelTabValue=SUBMISSION
# Similar to hare and tortise. Just the hare first moves till the deleted item and then move hare and tortise by 1:
def removeKthNode(head, k):
    
    if head == None:
        return None
    fast = head
    slow = head
    for i in range(k):
        fast = fast.next
    
    if fast is None:
        return head.next
    
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next
    return head