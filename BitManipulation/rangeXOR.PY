# Question: https://www.codingninjas.com/studio/problems/l-to-r-xor_8160412?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION


# Approach:
# To find the XOR of all numbers in the range [L, R] using bit manipulation, we can leverage a few properties of XOR:

# XOR of a number with itself is 0.
# XOR of a number with 0 is the number itself.
# XOR operation is associative and commutative, which means the order of operations does not change the result.
# Moreover, there's a pattern in the XOR of numbers from 0 to n, which we can use to our advantage. Specifically:

# XOR(0 to n) = n, if n % 4 == 0
# XOR(0 to n) = 1, if n % 4 == 1
# XOR(0 to n) = n + 1, if n % 4 == 2
# XOR(0 to n) = 0, if n % 4 == 3
# With this pattern, we can find the XOR of all numbers from 0 to L-1 and from 0 to R, and then XOR these two results to get the XOR of the range [L, R]. This works because XORing [0, L-1] with [0, R] cancels out the XOR of [0, L-1], effectively leaving us with the XOR of [L, R].

# Here's how to implement this solution:

# Define a function to find the XOR of all numbers from 0 to n.
# Use this function to find XOR(0 to L-1) and XOR(0 to R).
# XOR these two results to get the answer
from typing import *

def findXOR(L : int, R : int) -> int:
    def xorRange(n):
        if n%4 == 0:
            return n
        if n%4 == 1:
            return 1
        if n%4 == 2:
            return n+1
        else:
            return 0
    
    def xor(l,r):
        return xorRange(l-1) ^ xorRange(r)
    
    return xor(L,R)