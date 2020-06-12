# Review the following link for the question prompt: https://leetcode.com/problems/generate-parentheses/

# O(n^2) time | O(logn) space
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        leftParenthesisCount = n
        rightParenthesisCount = n
        results = []
        
        self.generateParenthesisRecursive(results, '', leftParenthesisCount, rightParenthesisCount)
        return results
    
    def generateParenthesisRecursive(self, results, current, leftParenthesisCount, rightParenthesisCount):
        
        if leftParenthesisCount == 0 and rightParenthesisCount == 0:
            results.append(current)
            return
        
        if leftParenthesisCount > 0:
            self.generateParenthesisRecursive(results, current + '(', leftParenthesisCount-1, rightParenthesisCount)
        if rightParenthesisCount > leftParenthesisCount:
            self.generateParenthesisRecursive(results, current + ')', leftParenthesisCount, rightParenthesisCount-1)
        return