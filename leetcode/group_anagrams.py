# Review the following link for the question prompt: https://leetcode.com/problems/group-anagrams/

# O(N + N * mlog(m)) time | O(N) space
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        memory = {}
        for anagram in strs:
            sorted_anagram = ''.join(sorted(anagram))
            if sorted_anagram in memory:
                memory[sorted_anagram].append(anagram)
            else:
                memory[sorted_anagram] = [anagram]
            
        results = []
        for value in memory.values():
            results.append(value)
        
        return results