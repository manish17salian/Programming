# Question: https://www.codingninjas.com/studio/problems/unique-element-in-sorted-array_1112654?leftPanelTabValue=SUBMISSION

def singleNonDuplicate(arr):
    # stack = []
    # for i in arr:
    #     popped = False
    #     while stack and stack[-1] == i:
    #         stack.pop()
    #         popped = True
    #     if not popped:
    #         stack.append(i)
    # return stack[0]
    left = 0
    right = len(arr)-1
    
    while left < right:
        mid = left + (right-left)//2

        if mid%2 == 1:
            mid-=1
        
        if arr[mid] == arr[mid+1]:
            left = mid+2
        else:
            right = mid
    
    return arr[left]


    
