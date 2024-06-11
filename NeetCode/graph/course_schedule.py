# Question: https://leetcode.com/problems/course-schedule/description/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        indegree = [0]*numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1
        
        queue = deque()
        for index, val in enumerate(indegree):
            if val == 0:
                queue.append(index)
        
        topo = []
        while queue:
            course = queue.popleft()
            topo.append(course)

            for cor in adj[course]:
                indegree[cor]-=1
                if indegree[cor] == 0:
                    queue.append(cor)

        if len(topo) != numCourses:
            return False
        else:
            return True  