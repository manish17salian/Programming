# Question:https://www.naukri.com/code360/problems/alien-dictionary_630423?leftPanelTabValue=SUBMISSION

from typing import List
from collections import *
def getAlienLanguage(dictionary: List[str], k: int) -> str:
    adj = defaultdict(list)
    for i in range(len(dictionary)-1):
        w1 = dictionary[i]
        w2 = dictionary[i+1]
        length = min(len(w1), len(w2))

        for j in range(length):
            if w1[j] != w2[j]:
                adj[ord(w1[j]) - ord('a')].append(ord(w2[j]) - ord('a'))
                break
    indegree = [0] * k
    for src in range(k):
        for dest in adj[src]:
            indegree[dest] += 1

    q = deque()
    for i in range(k):
        if indegree[i] == 0:
            q.append(i)

    topo = []
    while q:
        node = q.popleft()
        topo.append(node)
        for it in adj[node]:
            indegree[it] -= 1
            if indegree[it] == 0:
                q.append(it)
    
    ans = "".join(chr(it + ord('a')) for it in topo)
    return ans
