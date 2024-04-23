# Question: https://leetcode.com/problems/is-graph-bipartite/submissions/1235825738/
# Solution: https://www.youtube.com/watch?v=KG5YFfR0j8A
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node, color, check):
            check[node] = color
            for i in graph[node]:
                if check[i] == -1:
                    if not dfs(i, 1-color, check):
                        return False
                elif check[i] == color:
                    return False
            return True


    
        check = [-1]*len(graph)

        for i in range(len(graph)):
            if check[i] == -1:
                if not dfs(i, 1, check):
                    return False
        return True
        