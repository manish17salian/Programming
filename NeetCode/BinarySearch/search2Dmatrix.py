# Question: https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def recurssion(left, right):
            if left > right:
                return False
            mid = (left+right)//2
            row = mid//len(matrix[0])
            col = mid % len(matrix[0])
            if target == matrix[row][col]:
                return True
            elif target <= matrix[row][col]:
                return recurssion(left, mid-1)
            else:
                return recurssion(mid+1, right)
                
        return recurssion(0, (len(matrix)*len(matrix[0]))-1)