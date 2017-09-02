"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Example :

n = 5
n! = 120
Number of trailing zeros = 1
So, return 1
"""

import math


class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        zero = 0
        count = 1

        while int(A / math.pow(5, count)) > 0:
            count += 1

        while count >= 1:
            zero += int(A / math.pow(5, count))
            count -= 1

        return zero


s = Solution()
assert s.trailingZeroes(125) == 31, "Houston, we have a problem"
print "Success!"

