"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the subarray.
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        maxSoFar = A[0]
        maxEndHere = 0
        start = 0
        end = 0

        for i in range(len(A)):
            maxEndHere += A[i]
            if maxSoFar < maxEndHere:
                maxSoFar = maxEndHere
                end = i
            if maxEndHere < 0:
                maxEndHere = 0
                start = i

        result = []

        while start < end :
            result.append(A[start + 1])
            start += 1

        return result


s = Solution()
t = (-2, 1, -3, 4, -1, 2, 1, -5, 4)
expected = [4,-1,2,1]

print s.maxSubArray(t)
assert s.maxSubArray(t) == expected, "Houston, we have a problem!"
print "Success!"
