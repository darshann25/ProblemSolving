"""
There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

Sample Input

A : [1 4 5]
B : [2 3]

Sample Output

3
"""

import sys


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, list1, list2):
        total = len(list1) + len(list2)
        if total % 2 == 0:
            return (
                   self.findKthElement(total / 2 + 1, list1, list2, 0, 0) + self.findKthElement(total / 2, list1, list2,
                                                                                                0, 0)) / 2.0
        else:
            return self.findKthElement(total / 2 + 1, list1, list2, 0, 0)

    def findKthElement(self, k, list1, list2, s1, s2):
        if s1 >= len(list1):
            return list2[s2 + k - 1]
        if s2 >= len(list2):
            return list1[s1 + k - 1]

        if k == 1:
            return min(list1[s1], list2[s2])

        m1 = s1 + k / 2 - 1
        m2 = s2 + k / 2 - 1

        mid1 = list1[m1] if m1 < len(list1) else sys.maxint
        mid2 = list2[m2] if m2 < len(list2) else sys.maxint

        if mid1 < mid2:
            return self.findKthElement(k - k / 2, list1, list2, m1 + 1, s2)
        else:
            return self.findKthElement(k - k / 2, list1, list2, s1, m2 + 1)

s = Solution()
l1 = [1, 4, 5]
l2 = [2, 3]

f1 = [5, 6, 8, 30, 35, 37]
f2 = [4, 7, 10, 20, 21, 22]

assert s.findMedianSortedArrays(l1, l2) == 3, "Houston, we have a problem."
print s.findKthElement(6, f1, f2, 0, 0)
print "Success!"
