# Review the following link for the question prompt: https://leetcode.com/problems/word-ladder-ii/

# O(N * m) time | O(b) space
from collections import defaultdict
from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return []
        
        # wordListCombinations = self.generateCombinations(wordList, beginWord)
        wordListCombinations = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                wordListCombinations[word[:i]+' '+word[i+1:]].append(word)
        
        ladders = []
        seen = set([beginWord])
        queue = deque([[beginWord, [beginWord]]])
        found = False
        
        while queue and not found:
            breadth = len(queue)
            seenAtLevel = set()
            
            for _ in range(breadth):
            
                x, q_item = queue.popleft()
                
                for i in range(len(x)):
                    for transform in wordListCombinations[x[:i] + ' ' + x[i+1:]]:
                        if transform == endWord:
                            ladders.append(q_item + [transform])
                            found = True
                        
                        if transform not in seen:
                            queue.append((transform, q_item + [transform]))
                            seenAtLevel.add(transform)
                    
            seen = seen.union(seenAtLevel)
            
        return ladders