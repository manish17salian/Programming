# Question: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/


from collections import defaultdict
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        
        ways = [0]*n
        distList = [float("inf")]*n

        ways[0] = 1
        distList[0] = 0
        mod = 10**9 + 7
        heap = []
        heapq.heappush(heap,(0,0))

        while heap:
            dist, node = heapq.heappop(heap)
            
            for conn, d in adj[node]:
                newD = d+dist

                if distList[conn] > newD :
                    distList[conn] = newD
                    heapq.heappush(heap, (newD, conn))
                    ways[conn] = ways[node]

                elif distList[conn] == newD:
                    ways[conn] = (ways[conn] + ways[node]) % mod
        
        return ways[n-1]


        