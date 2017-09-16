"""
Given an input string, reverse the string word by word.

Example:

Given s = "the sky is blue",

return "blue is sky the".

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.
"""


class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, str):
        string = list(reversed(str))

        start = 0
        end = 0

        for end in range(len(string) + 1):
            if end == len(string) or string[end] == " ":
                string[start:end] = reversed(string[start:end])
                start = end + 1

        return "".join(string)


s = Solution()
input = "the sky is blue"
output = "blue is sky the"
assert s.reverseWords(input) == output, "Houston, we have a problem!"
print "Success!"

