# Question: https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        indegree = [0]*numCourses
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)
            for course in adj[node]:
                indegree[course] -=1
                if indegree[course] == 0:
                    queue.append(course)

        if len(topo) == numCourses:
            return topo
        else:
            return []