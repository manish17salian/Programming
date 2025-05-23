# Question: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        
        def gcd(a,b):
            while b:
                a,b = b, a%b
            return a

        res = gcd(len(str1), len(str2))
        return str1[:res]
        