"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example :

Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Rain water trapped: Example 1

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):

        i = len(A) - 1
        left = [None] * (i + 1)
        right = [None] * (i + 1)

        maxR = A[i]
        maxL = A[0]

        while i >= 0:
            if A[i] > maxR:
                maxR = A[i]
            right[i] = maxR
            i -= 1

        i = 0
        while i < len(A):
            if A[i] > maxL:
                maxL = A[i]
            left[i] = maxL
            i += 1

        i = 0
        water = 0

        for i in range(len(A)):
            water += min(left[i], right[i]) - A[i]

        return water


s = Solution()
input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
assert s.trap(input) == 6, "Houston, we have a problem!"
print "Success!"
