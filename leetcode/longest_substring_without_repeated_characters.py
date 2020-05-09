# Review the following link for the question prompt: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# O(N) time | O(min(N,A)) space
class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        maxSubstring = ''
        runningSubstring = ''
        memory = {}

        startIdx = 0
        endIdx = 0

        for i, newChar in enumerate(string):
            endIdx = i
            if newChar in memory:

                startIdx = max(startIdx, memory[newChar] + 1)
            memory[newChar] = endIdx

            runningSubstring = string[startIdx : endIdx + 1]

            if len(runningSubstring) >= len(maxSubstring):
                maxSubstring = runningSubstring

        return len(maxSubstring)