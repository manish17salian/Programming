# Question: https://www.codingninjas.com/studio/problems/allocate-books_1090540?leftPanelTabValue=SUBMISSION    

def findPages(arr: [int], n: int, m: int) -> int:
    if m > n:
        return -1

    def checkStudent(num):
        count = 0
        studentCount = 1
        for i in arr:
            if i+count <= num:
                count+=i
            else:
                studentCount+=1
                count = i
        return studentCount

    def binary(left, right):
        if left > right:
            return left
        
        mid = (left+right)//2
        val = checkStudent(mid)
        if val > m:
            return binary(mid+1, right)
        else:
            return binary(left, mid-1)
    return binary(max(arr), sum(arr))