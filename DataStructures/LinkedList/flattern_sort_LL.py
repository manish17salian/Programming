# Question: 'https://www.codingninjas.com/studio/problems/flatten-a-linked-list_1112655?leftPanelTab=1'


class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.
def flattenLinkedList(head: Node) -> Node:
    # create a pointer to track the current node
    current = head
    # loop until the current node is None
    while current:
        # if the current node has a child node, insert it between the current node and its next node
        if current.child:
            # save the next node of the current node
            next = current.next
            # set the next node of the current node to its child node
            current.next = current.child
            # set the child pointer of the current node to None
            current.child = None
            # find the tail of the child list
            tail = current.next
            while tail.next:
                tail = tail.next
            # connect the tail of the child list to the next node of the current node
            tail.next = next
        # move to the next node
        current = current.next
    # return the head of the flattened list
    
    def merge_sort(head):
        if not head or not head.next:
            return head

        # Find the middle of the linked list
        middle = find_middle(head)

        # Split the linked list into two halves
        left_half = head
        right_half = middle.next
        middle.next = None

        # Recursively sort the two halves
        left_sorted = merge_sort(left_half)
        right_sorted = merge_sort(right_half)

        # Merge the sorted halves
        return merge(left_sorted, right_sorted)

    def find_middle(head):
        slow_ptr = head
        fast_ptr = head

        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr

    def merge(left, right):
        dummy = Node()
        current = dummy

        while left and right:
            if left.data < right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        # Append any remaining elements from both lists
        if left:
            current.next = left
        if right:
            current.next = right

        return dummy.next
    sorted_head = merge_sort(head)
    return sorted_head


