import math
def minimumRateToEatBananas(v: [int], h: int) -> int:
    if sum(v) < h:
        return min(v)
    
    def getElement(num):
        count = 0
        for i in v:
            count  += math.ceil(i/num)
        return count
    maxEl = max(v)
    def binarySearch(left, right):
        if left >= right:
            return left
        mid = (left+right)//2
        val = getElement(mid)
        if val > h:
            return binarySearch(mid+1, right)
        else:
            return binarySearch(left, mid)       
    
    return binarySearch(1, maxEl)


print(minimumRateToEatBananas([4, 9, 4, 3, 1, 3 ], 66))