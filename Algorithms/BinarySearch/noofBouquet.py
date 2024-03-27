# Question: https://www.codingninjas.com/studio/problems/rose-garden_2248080?count=25&page=4&search=&sort_entity=order&sort_order=ASC&attempt_status=COMPLETED&leftPanelTabValue=SUBMISSION

from typing import List
def roseGarden(arr: List[int], r: int, b: int):
    def checkBouquet(day):
        count = 0
        noOfBouquet = 0
        for i in arr:
            if i <= day:
                count+=1
            if i > day:
                noOfBouquet+= count//r
                count = 0
        noOfBouquet += count // r
        return noOfBouquet
                
    def binarySearch(left, right):
        if left > right:
            return left
        mid = (left+right)//2
        value = checkBouquet(mid)
        if value < b:
            return binarySearch(mid+1, right)
        else:
            return binarySearch(left, mid-1)

    
    max_day = max(arr)
    result = binarySearch(min(arr), max_day)
    return result if checkBouquet(result) >= b else -1