class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = 'aeiou'

        for char in vowels:
            S = S.replace(char,"")

        return S

s = Solution()
assert s.removeVowels("leetcodeisacommunityforcoders") == "ltcdscmmntyfrcdrs", "Houston, we have a problem!"
print("Success!")
