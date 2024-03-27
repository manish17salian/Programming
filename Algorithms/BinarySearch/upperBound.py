# Question: https://www.codingninjas.com/studio/problems/implement-upper-bound_8165383?leftPanelTabValue=SUBMISSION
def upperBound(arr: [int], x: int, n: int) -> int:
    
    def binary(left, right):
        if left == right:
            return left
        mid = (left+right)//2
        if arr[mid] > x:
            return binary(left, mid)
        else:
            return binary(mid+1, right)
    return binary(0, len(arr))
arr = [2,4,6,7]
x = 5
print(upperBound(arr, x))