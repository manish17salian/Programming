# Question: https://leetcode.com/problems/hand-of-straights/submissions/1221341907/
# Solution: https://www.youtube.com/watch?v=amnrMCVd2YI

from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        countDict = Counter(hand)
        minHeap = list(countDict.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first+groupSize):
                if i not in countDict:
                    return False

                countDict[i]-=1
                if countDict[i] == 0:
                    if i != minHeap[0]:
                        return False
                    else:
                        heapq.heappop(minHeap)
        return True
        