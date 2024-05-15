# Question: https://www.naukri.com/code360/problems/floyd-warshall_2041979?leftPanelTabValue=SOLUTION

def floydWarshall(n, m, src, dest, edges):
    matrix = [[float("inf")]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        matrix[i][i] = 0
    
    for u, v, w in edges:
        matrix[u][v] = w
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if matrix[i][k] != float("inf") and  matrix[k][j] != float("inf"):
                    matrix[i][j] = min(matrix[i][k] + matrix[k][j], matrix[i][j])
    

    if matrix[src][dest] == float("inf"):
        return 1000000000
    else:
        return matrix[src][dest]

    


        
    




    


        
    


