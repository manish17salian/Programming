# Question: https://www.codingninjas.com/studio/problems/occurrence-of-x-in-a-sorted-array_630456?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

def count(arr: [int], n: int, x: int) -> int:

    def binarySearchFirst(left, right):
        if left > right:
            return -1
        mid = (left+right)//2
        if arr[mid] == x:
            if mid == 0 or arr[mid-1] < x:
                return mid
            else:
                return binarySearchFirst(left, mid-1)
        elif arr[mid] >= x:
            return binarySearchFirst(left, mid-1)
        else:
            return binarySearchFirst(mid+1, right)

    def binarySearchLast(left, right):
        if left > right:
            return -1
        mid = (left+right)//2
        if arr[mid] == x:
            if mid == n-1 or arr[mid+1] > x:
                return mid
            else:
                return binarySearchLast(mid+1, right)
        elif arr[mid] > x:
            return binarySearchLast(left, mid-1)
        else:
            return binarySearchLast(mid+1, right)
    
    first = binarySearchFirst(0, n-1)
    last = binarySearchLast(0, n-1)
    
    if first == -1 or last == -1:
        return 0  # x not found
    else:
        return last - first + 1
    
# Binary Search for First Occurrence
# The function binarySearchFirst is designed to find the first occurrence of x in the sorted array. It does this by recursively searching the array, narrowing down the search range until it finds the first index where x appears. If x is found and it is either the first element of the array or the element before it is less than x, this index is returned as the first occurrence.

# This function is essential for counting because it helps identify the starting point of x in the array.

# Binary Search for Last Occurrence
# Similarly, binarySearchLast looks for the last occurrence of x. It follows the same binary search principle but checks if the found instance of x is either the last element of the array or the next element is greater than x. If so, this indicates the last occurrence of x.

# Finding the last occurrence is crucial because it marks the endpoint of x in the array.

# Counting Occurrences
# The actual "counting" happens after both the first and last occurrences of x are identified. If either first or last is -1, it means x was not found in the array, and the function returns 0.

# If both first and last are valid indices (not -1), the count of x in the array can be determined by subtracting first from last and adding 1 (since array indices start at 0). This calculation effectively counts the number of elements between the first and last occurrences of x, inclusive.