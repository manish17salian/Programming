def majorityElement(self, nums: List[int]) -> int:
    num = None
    count = 0

    for i in nums:
        if count == 0:
            count+=1
            num = i
        elif num != i:
            count -= 1
        else:
            count +=1
    
    return num