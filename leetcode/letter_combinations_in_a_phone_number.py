# Review the following link for the question prompt: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# O(n^2) time | O(n^n) space
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if len(digits) == 0 or not digits:
            return result
        
        mapping = [0,1,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        self.letterCombinationsRecursive(result, digits, '', 0, mapping)
        return result
    
    def letterCombinationsRecursive(self, result, digits, current, index, mapping):
        if index == len(digits):
            result.append(current)
            return
        
        letters = mapping[int(digits[index])]
        for letter in letters:
            self.letterCombinationsRecursive(result, digits, current + letter, index + 1, mapping)
        return       