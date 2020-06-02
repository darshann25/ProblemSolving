# Review the following link for the question prompt: https://leetcode.com/problems/first-unique-character-in-a-string/

# O(N) time | O(N) space
class Solution:
    def firstUniqChar(self, s: str) -> int:
        charDict = {}
        
        for idx, char in enumerate(s):
            if char in charDict:
                charDict[char] += 1
            else:
                charDict[char] = 1
        
        for idx, char in enumerate(s):
            if charDict[char] == 1:
                return idx
        
        return -1