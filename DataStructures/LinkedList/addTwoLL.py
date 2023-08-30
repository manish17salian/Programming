# Question: https://www.codingninjas.com/studio/problems/add-two-numbers_1170520?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    # Write your code here.
    dummy1 = head1
    dummy2 = head2

    firtNumber = None
    secondNumber = None
    current = None

    count1 = 0
    count2 = 0
    while head1:
        count1 += 1
        head1 = head1.next
    while head2:
        count2 += 1
        head2 = head2.next
    
    if count1 > count2:
        firtNumber = dummy1
        secondNumber = dummy2
    elif count2 > count1:
        firtNumber = dummy2
        secondNumber = dummy1
    else:
        firtNumber = dummy1
        secondNumber = dummy2

    count = 0
    node = None
    head = None
    prev = None
    carry = 0
    while firtNumber:
        # if count == 1:
        #     print(firtNumber.data, secondNumber.data, carry, 'Lets check')
        if (secondNumber):
            sumation = firtNumber.data + secondNumber.data + carry
        else:
            sumation = firtNumber.data + carry
        # print(sumation, '-----')
        
        if sumation > 9:
            carry = 1
            newNode = Node(sumation-10)
        else:
            carry = 0
            newNode = Node(sumation)

        if (firtNumber.next==None and carry == 1):
            newNode.next = Node(1)
        
        if prev == None:
            node = newNode
            prev = node
        else:
            prev.next = newNode
            prev = prev.next
        # print(node.data, '---')
        

        firtNumber = firtNumber.next
        if (secondNumber and secondNumber.next):
            secondNumber = secondNumber.next
        else:
            secondNumber = None
        count+=1
        # node.next = Node()
    return node

    

    
    