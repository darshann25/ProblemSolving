# Review the following link for the question prompt: https://leetcode.com/problems/word-ladder/

# O(N * m) time | O(b) space
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        level = 0
        queue = [beginWord]
        
        while len(queue) != 0:
            breadth = len(queue)
            
            for i in range(breadth):
            
                word = queue.pop(0)
                if word == endWord:
                    return level + 1
                
                validTransforms, wordList = self.checkValidTransforms(word, wordList)
                for transform in validTransforms:
                    queue.append(transform)
            level += 1
        return 0
    
    def checkValidTransforms(self, word: str, wordList: List[str]):
        
        transforms = []
        
        for currWord in wordList:
            wordDiff = 0
            for i in range(len(word)):
                if word[i] != currWord[i]:
                    wordDiff += 1
                    if wordDiff > 1:
                        break
            
            if wordDiff == 1:
                transforms.append(currWord)
        
        updatedWordList = [x for x in wordList if x not in transforms]
        return transforms, updatedWordList