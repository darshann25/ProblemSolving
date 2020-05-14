# Review the following link for the question prompt: https://leetcode.com/problems/longest-palindromic-substring/

# With DP - O(N^2) time | O(N^2) space
# Without DP - O(N^2) time | O(1) space

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s: return s
        
        strLen = len(s)
        dp = [[0] * strLen for i in range(strLen)]
        maxLen = 1
        maxStr = s[0]
        
        for i in range(strLen):
            dp[i][i] = 1
                    
        for length in range(2, strLen + 1):
            
            for i in range(strLen - length + 1):
                j = i + length - 1
                if abs(i - j) == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    maxLen = length
                    maxStr = s[i:j+1]
                
                elif s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                    maxLen = length
                    maxStr = s[i:j+1]
                else:
                    dp[i][j] = 0
                                
        return maxStr
    
    def longestPalindromeNoDP(self, string: str) -> str:
        currentLongest = [0,1]
        for i in range(len(string)):
            odd = self.getLongestPalindrome(string, i-1, i+1)
            even = self.getLongestPalindrome(string, i-1, i)
            longest = max(odd, even, key = lambda x: x[1] - x[0])
            currentLongest = max(currentLongest, longest, key = lambda x: x[1] - x[0])
        return string[currentLongest[0]: currentLongest[1]]

    def getLongestPalindrome(self, string, startIdx, endIdx):
        while startIdx >= 0 and endIdx < len(string):
            if string[startIdx] != string[endIdx]:
                break
            startIdx -= 1
            endIdx += 1
        return [startIdx + 1, endIdx]