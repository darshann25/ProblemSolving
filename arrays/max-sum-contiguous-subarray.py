"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        maxSoFar = A[0]
        maxEndHere = 0

        for i in range(len(A)):
            maxEndHere += A[i]
            if maxSoFar < maxEndHere: maxSoFar = maxEndHere
            if maxEndHere < 0: maxEndHere = 0

        return maxSoFar


s = Solution()
t = (-2, 1, -3, 4, -1, 2, 1, -5, 4)

assert s.maxSubArray(t) == 6, "Houston, we have a problem!"
print "Success!"
