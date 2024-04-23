# Question: https://leetcode.com/problems/find-median-from-data-stream/
# Soltion: https://www.youtube.com/watch?v=itmhHWaHupI


import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -1*num)
        
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -1*heapq.heappop(self.left))
        
        if len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left, -1*heapq.heappop(self.right))

        
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -1 * self.left[0]
        if len(self.right) > len(self.left):
            return self.right[0]
        if len(self.right) == len(self.left):
            return ((-1*self.left[0]) + (self.right[0]))/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()