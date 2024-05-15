# Question: https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/1243499279/

def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    adj = defaultdict(list)
    for u,v,w in flights:
        adj[u].append((v,w))
    heap = []
    heapq.heappush(heap, (0,src,0))

    distList = [float("inf")]*n
    distList[src] = 0

    while heap:
        cost, node, stop = heapq.heappop(heap)
        if node == dst:
            return cost
        
        if stop > k:
            continue

        for conn, w in adj[node]:
            nCost = w+cost
            if nCost < distList[conn] and stop <= k:
                distList[conn] = nCost
                heapq.heappush(heap, (nCost, conn, stop+1))
    
    return -1 if distList[dst] == float('inf') else distList[dst]