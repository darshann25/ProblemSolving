"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

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
