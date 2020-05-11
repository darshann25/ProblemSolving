# Review the following link for the question prompt: https://leetcode.com/problems/implement-strstr/

# O(N+m) time | O(1) space
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)