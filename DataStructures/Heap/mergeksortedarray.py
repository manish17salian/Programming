# Question: https://www.naukri.com/code360/problems/merge-k-sorted-arrays_975379?leftPanelTabValue=SUBMISSION

from sys import *
from collections import *
from math import *
import heapq

def mergeKSortedArrays(kArrays, k:int):
	minHeap = []
	result = []

	for i, arr in enumerate(kArrays):
		if arr:
			heapq.heappush(minHeap, (arr[0], i, 0))
	
	while minHeap:
		val, arrIdx, valIdx =  heapq.heappop(minHeap)
		result.append(val)
		
		if valIdx+1 < len(kArrays[arrIdx]):
			nextVal = kArrays[arrIdx][valIdx+1]
			heapq.heappush(minHeap, (nextVal, arrIdx, valIdx+1))
	
	return result