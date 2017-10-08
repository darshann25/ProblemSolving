"""
Given an array of integers, find the length of longest subsequence which is first increasing then decreasing.

**Example: **

For the given array [1 11 2 10 4 5 2 1]

Longest subsequence is [1 2 10 4 2 1]

Return value 6
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        if len(A) == 0 or len(A) == 1 : return len(A)

        inc_sub = [1] * len(A)
        dec_sub = [1] * len(A)
        maxLen = 1

        for i in range(1, len(A)) :
            for j in range(0, i) :
                if A[i] > A[j]:
                    value = inc_sub[j]
                    if(inc_sub[i] < value + 1):
                        inc_sub[i] = value + 1

        for i in range(len(A) - 2, -1, -1):
            for j in range(len(A) - 1, i, -1):
                if A[i] > A[j]:
                    value = dec_sub[j]
                    if(dec_sub[i] < value + 1):
                        dec_sub[i] = value + 1

        for i in range(len(A)):
            currmax = inc_sub[i] + dec_sub[i] - 1
            if currmax > maxLen:
                maxLen = currmax

        return maxLen


s = Solution()
input = (1, 11, 2, 10, 4, 5, 2, 1)
assert s.longestSubsequenceLength(input) == 6, "Houston, we have a problem!"
print "Success!"
