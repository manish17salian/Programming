# Question: https://neetcode.io/problems/valid-tree
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False  # A valid tree must have exactly n-1 edges
        if len(edges) == 0:
            return True
            
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegree[a] += 1
            indegree[b] += 1

        queue = deque()
        for index, val in enumerate(indegree):
            if val == 1:  # Start from leaf nodes
                queue.append(index)
        
        visited = set()
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 1 and neigh not in visited:
                    queue.append(neigh)
        return len(visited) == n
