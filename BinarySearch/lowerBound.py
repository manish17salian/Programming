# Questions: https://www.codingninjas.com/studio/problems/lower-bound_8165382?leftPanelTabValue=SOLUTION

def lowerBound(arr: [int], n: int, x: int) -> int:
    def binary(left, right):
        if left == right:
            return left
        mid = (left+right)//2
        if arr[mid] >= x:
            return binary(left, mid)
        else:
            return binary(mid+1, right)
    return binary(0, len(arr))
arr = [1, 2, 2, 3]
x = 0
print(lowerBound(arr, x))  