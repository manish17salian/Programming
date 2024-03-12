# Question: https://www.codingninjas.com/studio/problems/aggressive-cows_1082559?leftPanelTabValue=SUBMISSION

def aggressiveCows(stalls, k):
    # Write your code here.
    stalls.sort()
    def checkPossibility(num):
        count = 1
        last = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i]-last >= num:
                count+=1
                last = stalls[i]
            if count >= k:
                return True
        return False
    def binary(left, right):
        if left > right:
            return right
        mid = (left+right)//2
        val = checkPossibility(mid)
        if not val:
            return binary(left, mid-1)
        else:
            return binary(mid+1, right)
    return binary(1, stalls[-1] - stalls[0])
