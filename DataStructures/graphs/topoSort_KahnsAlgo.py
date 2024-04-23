# Question: https://www.naukri.com/code360/problems/topological-sorting_973003

# DFS
def topologicalSort(adj, V, E):
    def dfs(node, stack, visited, adj):
        visited[node] = 1
        for nodes in adj[node]:
            if visited[nodes] == 0:
                dfs(nodes, stack, visited, adj)
        stack.append(node)

    def topo(adj, V):
        visited = [0]*V
        stack = []
        for node in range(V):
            if visited[node] == 0:
                dfs(node, stack, visited, adj)
        return stack
    stack = topo(adj, V)
    answer = []
    while stack:
        answer.append(stack.pop())
    return answer



# Kahns Algo/Bfs
from collections import deque

def topologicalSort(adj, V, E):
    indegArr = [0]*V
    for node in range(V):
        for nodes in adj[node]:
            indegArr[nodes] +=1
    
    queue = deque()

    
    for i in range(V):
        if indegArr[i] == 0:
            queue.append(i)
    
    answer = []
    
    while queue:
        node = queue.popleft()
        answer.append(node)

        for nodes in adj[node]:
            indegArr[nodes]-=1
            if indegArr[nodes] == 0:
                queue.append(nodes)
    
    if len(answer) != V:
        raise ValueError("There exists a cycle in the graph, so topological sorting is not possible")

    return answer
            


