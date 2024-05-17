# Question: https://leetcode.com/problems/koko-eating-bananas/description/


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxCount = max(piles)
        if len(piles) == 1:
            return ceil(piles[0]/h)
        if sum(piles) < h:
            return min(piles)

        def checkCount(val):
            count = 0
            for i in piles:
                count+= math.ceil(i/val)
            return count
        
        def recurssion(left, right):
            if left >= right:
                return left
            mid=(left+right)//2
            noOfB = checkCount(mid)
            if noOfB > h:
                return recurssion(mid+1, right)
            else:
                return recurssion(left, mid)  
        return recurssion(1, maxCount)

        