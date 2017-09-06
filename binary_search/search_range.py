# coding=utf-8
"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example:

Given [5, 7, 7, 8, 8, 10]

and target value 8,

return [3, 4].
"""


def binarySearch(list, low, high, target):
    while low <= high:
        mid = (low + high) / 2

        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers

    def searchRange(self, A, B):

        start = -1
        end = -1

        target = B
        low = 0
        high = len(A) - 1

        searchIndex = binarySearch(A, low, high, target)
        startIndex = searchIndex
        endIndex = searchIndex

        while startIndex != -1:
            start = startIndex
            if startIndex == 0: break
            startIndex = binarySearch(A, low, startIndex - 1, target)

        while endIndex != -1:
            end = endIndex
            if endIndex == len(A) - 1: break
            endIndex = binarySearch(A, endIndex + 1, high, target)

        return [start, end]


list = [5, 7, 7, 8, 8, 10]
target = 8
s = Solution()
assert s.searchRange(list, target) == [3, 4], "Houston, we have a problem!"
print "Success!"
