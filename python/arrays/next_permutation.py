# coding=utf-8
"""
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers.

If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.

The replacement must be in-place, do not allocate extra memory.

Examples:

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

20, 50, 113 → 20, 113, 50
Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

"""

class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        pivot = len(A) - 1

        while pivot >= 0 and A[pivot - 1] > A[pivot]:
            pivot -= 1
        if pivot == 0:
            return A[::-1]

        start = pivot
        end = len(A) - 1
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1

        seeker = pivot
        while A[seeker] < A[pivot - 1]:
            seeker += 1
        A[seeker], A[pivot - 1] = A[pivot - 1], A[seeker]

        return A

s = Solution()
assert s.nextPermutation([7, 5, 3, 8, 2]) == [7, 5, 8, 2, 3], "Houston, we have a problem!"
print "Success!"
