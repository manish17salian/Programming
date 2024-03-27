# Question: https://www.codingninjas.com/studio/problems/search-in-a-2d-matrix_980531?leftPanelTabValue=SUBMISSION

# ROW, COL is the important concept

def searchMatrix(matrix: [[int]], target: int) -> bool:


    def binary(left, right):
        if left > right:
            return False
        mid = (left+right)//2
        row = mid//len(matrix[0])
        col = mid%len(matrix[0])
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            return binary(mid+1, right)
        else:
            return binary(left, mid-1)
    
    return binary(0, len(matrix)*len(matrix[0])-1)


# Other Solution
    # noOfRows = len(matrix)
    # noOfCols = len(matrix[0])
    # row = 0
    # col = noOfCols-1


    # while row < noOfRows and col >= 0:
    #     if matrix[row][col] == target:
    #         return 1
    #     elif matrix[row][col] < target:
    #         row+=1
    #     else:
    #         col-=1
    # return False
    
    # def binary(left, right, arr):
    #     if left > right:
    #         return False
    #     mid = (left+right)//2
    #     if mid == target:
    #         return True
    #     elif arr[mid] > target:
    #         return binary(left, mid-1, arr)
    #     else:
    #         return binary(mid+1, right, arr)

    
    # condition = [False]
    # for i in mat:
    #     if i[-1] >= target:
    #         if i[-1] == target:
    #             return True
    #         else:
    #             condition[0] = binary(0, len(i)-1, i)
    # return condition[0]

