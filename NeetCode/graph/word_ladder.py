# Question: https://leetcode.com/problems/word-ladder/


from collections import *
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Create a dictionary to hold patterns and their corresponding words.
        patternDict = defaultdict(list)
        
        # Populate the pattern dictionary.
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patternDict[pattern].append(word)
        
        # BFS initialization
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while queue:
            current_word, steps = queue.popleft()
            
            # Check if we have reached the target word
            if current_word == endWord:
                return steps
            
            # Generate all possible patterns for the current word.
            for i in range(len(current_word)):
                pattern = current_word[:i] + "*" + current_word[i+1:]
                
                # Iterate through all words that match this pattern.
                for neighbor in patternDict[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))
        
        # If no transformation sequence is found, return 0.
        return 0



    
        