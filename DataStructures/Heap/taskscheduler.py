# Question: https://www.naukri.com/code360/problems/task-scheduler_1070424?leftPanelTabValue=SUBMISSION
# solution: https://www.youtube.com/watch?v=s8p8ukTyA2I
from os import *
from sys import *
from collections import *
from math import *
import heapq

def taskScheduler(tasks, t, n):
    counter = Counter(tasks)
    que = deque()

    time = 0

    maxHeap = [-cnt for cnt in counter.values()]
    heapq.heapify(maxHeap)

    while maxHeap or que:
        time+=1
        if maxHeap:
            cnt = 1+heapq.heappop(maxHeap)
            if cnt:
                que.append([cnt, time+n])
        
        if que and que[0][1] == time:
            heapq.heappush(maxHeap, que.popleft()[0])
    
    return time
    