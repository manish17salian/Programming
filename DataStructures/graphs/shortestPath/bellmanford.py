# Question: https://www.naukri.com/code360/problems/bellman-ford_2041977

from collections import *
from math import *

def bellmonFord(n, m, src, edges):
    d = [100000000 for i in range(n + 1)]

    # Distance of source to source is 0.
    d[src] = 0

    # Apply bellmonford algorithm.
    for i in range(1, n):

        for j in range(m):

            u = edges[j][0]
            v = edges[j][1]
            w = edges[j][2]

            if (d[u] != 1000000000 and d[v] > (d[u] + w)):
                d[v] = d[u] + w

    # Return the distance of destination.
    return d
