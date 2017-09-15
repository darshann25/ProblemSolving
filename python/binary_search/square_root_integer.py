"""
Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY
"""


class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 1: return A

        start = 0
        end = A
        val = A

        while True:
            mid = (start + end) / 2

            sqr = mid * mid
            if sqr == val: return mid

            if sqr > val:
                end = mid
            else:
                higher = (mid + 1) * (mid + 1)
                if higher > val: return mid
                start = mid


s = Solution()
assert s.sqrt(3969) == 63, "Houston, we have a problem!"
print "Success!"
