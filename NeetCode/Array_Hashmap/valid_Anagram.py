# Question:https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for letter in s:
            if letter in hashmap:
                hashmap[letter]+=1
            else:
                hashmap[letter] = 1

        for letter in t:
            if letter in hashmap:
                hashmap[letter]-=1
                if hashmap[letter] == 0:
                    del hashmap[letter]
            else:
                return False
        
        if not hashmap:
            return True
        else:
            return False

        