# Question: https://www.codingninjas.com/studio/problems/rotation_7449070?leftPanelTabValue=SUBMISSION
# Hint: Find the position of Minimum Element

def findKRotation(arr : [int]) -> int:
    # def binarySearch(dividedArr):
    #     if len(dividedArr) == 1:
    #         return dividedArr[0]
    #     mid = len(dividedArr)//2
    #     leftPart = dividedArr[:mid]
    #     rightPart = dividedArr[mid:]
    #     if len(dividedArr) == 1:
    #         return mid

    #     if leftPart[-1] > rightPart[-1]:
    #         return binarySearch(rightPart)
    #     else:
    #         return binarySearch(leftPart)
    # return binarySearch(arr)
    left = 0
    right = len(arr)-1

    while left < right:
        mid = (left+right)//2
        if arr[mid] > arr[right]:
            left = mid+1
        else:
            right = mid
    
    return left
