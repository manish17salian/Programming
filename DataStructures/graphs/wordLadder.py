# Question: https://leetcode.com/problems/word-ladder/

from collections import *
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patternDict = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*"+ word[j+1:]
                patternDict[pattern].append(word)
        visit = set([beginWord])
        queue = deque([(beginWord,1)])

        while queue:
            curr_word,dept = queue.popleft()
            if curr_word == endWord:
                return dept
            for j in range(len(curr_word)):
                pattern = curr_word[:j] + "*"+ curr_word[j+1:]
                for word in patternDict[pattern]:
                    if word not in visit:
                        visit.add(word)
                        queue.append([word, dept+1])
        return 0


    
        