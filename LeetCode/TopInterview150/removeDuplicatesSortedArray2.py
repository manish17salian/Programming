def removeDuplicates(self, nums: List[int]) -> int:
    leftPointer = 2 
    for rightPointer in range(2, len(nums)):
        if nums[rightPointer] != nums[leftPointer - 2]:  
            nums[leftPointer] = nums[rightPointer]
            leftPointer += 1  

    return leftPointer 
    