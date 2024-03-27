# Question: https://www.codingninjas.com/studio/problems/painter-s-partition-problem_1089557?leftPanelTabValue=SUBMISSION

def findLargestMinDistance(boards:list, k:int):

    def checkPainter(num):
        count = 1
        totalTime = 0
        for i in boards:
            if totalTime + i <= num:
                totalTime+=i
            else:
                totalTime = i
                count+=1
        return count
    def binary(left, right):
        if left > right:
            return left
        mid = (left+right)//2
        val = checkPainter(mid)
        if val > k:
            return binary(mid+1, right)
        else:
            return binary(left, mid-1)
    
    return binary(max(boards), sum(boards))