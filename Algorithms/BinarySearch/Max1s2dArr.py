# Question: https://www.codingninjas.com/studio/problems/row-of-a-matrix-with-maximum-ones_982768?leftPanelTabValue=SUBMISSION

"""
    Time Complexity: O(N * M)
    Space Complexity: O(1)

    Where N is the number of rows and M is the number of columns in the given matrix.
"""


def rowWithMax1s(matrix: [[int]], n: int, m: int) -> int:

    def binary(left, right, arr):
        if left >= right:
            return len(arr)-left
        mid = (left+right)//2
        if arr[mid]==1:
            return binary(left, mid, arr)
        else:
            return binary(mid+1, right, arr)
    count = [0]
    index = -1
    for ind, i in enumerate(matrix):
        if count[0] < binary(0, len(i), i): 
            count[0] = max(count[0], binary(0, len(i)-1, i))
            index = ind
    return index



    # #    maxCount stores the maximum number of 1s found till now and ans is the index of that particular row.
    # maxCount = 0
    # ans = -1

    # for i in range(n):
    #     #    Count for number of ones for the current row.
    #     curr = 0
    #     for j in range(m):
    #         #   Increment count if the value is 1.
    #         if matrix[i][j] == 1:
    #             curr += 1

    #     #    Update curr row and maximum count if the current row has the maximum number of ones.
    #     if curr > maxCount:
    #         ans = i
    #         maxCount = curr

    # #    Return the row with maximum number of ones.
    # return ans
    