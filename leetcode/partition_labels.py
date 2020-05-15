# Review the following link for the question prompt: https://leetcode.com/problems/partition-labels/

# O(N) time | O(N) space
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        letterMemory = {}
        for idx, char in enumerate(S):
            if char in letterMemory:
                letterLimits = letterMemory[char]
            else:
                letterLimits = [float('inf'), float('-inf')]
            letterLimits[0] = min(letterLimits[0], idx)
            letterLimits[1] = max(letterLimits[1], idx)
            letterMemory[char] = letterLimits
        
        partitions = []
        minHolder = float('inf')
        maxHolder = float('-inf')
        
        for idx, char in enumerate(S):
            minHolder = min(minHolder, letterMemory[char][0])
            maxHolder = max(maxHolder, letterMemory[char][1])
            
            if idx == maxHolder:
                partitions.append(maxHolder - minHolder + 1)
                minHolder = float('inf')
                maxHolder = float('-inf')
        
        return partitions