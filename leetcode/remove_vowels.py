"""
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""


Note:

S consists of lowercase English letters only.
1 <= S.length <= 1000
"""

# Time Complexity: O(n)
# Space Complexity: o(1)

class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = 'aeiou'

        for char in vowels:
            S = S.replace(char,"")

        return S

s = Solution()
assert s.removeVowels("leetcodeisacommunityforcoders") == "ltcdscmmntyfrcdrs", "Houston, we have a problem!"
print("Success!")
