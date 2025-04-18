def removeDuplicates(self, nums: List[int]) -> int:
    leftPointer = 0
    for rightPointer in range(1, len(nums)):
        if nums[leftPointer] != nums[rightPointer]:
            leftPointer +=1
            nums[leftPointer] = nums[rightPointer]
    
    return leftPointer+1