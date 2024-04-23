# Question: https://www.naukri.com/code360/problems/find-the-number-of-states_1377943?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from typing import List

def findNumOfProvinces(roads: List[List[int]], n: int) -> int:

    def dfs(node):
        for index, val in enumerate(roads[node]):
            if val == 1 and not visited[index]:
                visited[index] = 1
                dfs(index)
    visited=[0]*n
    province = 0

    for city in range(n):
        if not visited[city]:
            dfs(city)
            province+=1
    
    return province
