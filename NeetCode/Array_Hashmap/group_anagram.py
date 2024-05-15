# Quetion: https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for words in strs:
            code = [0]*26
            for letter in words:
                code[ord(letter)-ord("a")]+=1
            res[tuple(code)].append(words)

        return res.values()
        