# Question: https://leetcode.com/problems/course-schedule-ii/submissions/1239051069/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            return True
        else:
            return False