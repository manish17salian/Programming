# Question: https://www.codingninjas.com/studio/problems/search-in-rotated-sorted-array_1082554?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

def search(arr, n, k):

    def binarySearch(left, right):
        if left > right:
            return -1  # Element not found
        mid = left + (right - left) // 2
       
        if arr[mid] == k:
           return mid
        
        if arr[left] <= arr[mid]:
            if arr[left] <= k < arr[mid]:
                return binarySearch(left, mid-1)
            else:
                return binarySearch(mid+1, right)
        else:
            if arr[mid] < k <= arr[right]:
                return binarySearch(mid+1, right)
            else:
                return binarySearch(left, mid-1)
    
    return binarySearch(0, n-1)
