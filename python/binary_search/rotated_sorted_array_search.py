"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?
"""


class Solution:
    # @param A : tuple of integers
    # @param target : integer
    # @return an integer
    def search(self, A, target):
        low = 0
        high = len(A) - 1

        while low <= high:
            mid = (high + low) / 2

            if A[mid] == target: return mid

            if A[low] <= A[mid]:
                if A[low] <= target < A[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            elif A[mid] < A[high]:
                if A[mid] < target <= A[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


s = Solution()
input = (4, 5, 6, 7, 0, 1, 2, 3)
target = 2

assert s.search(input, target) == 6, "Houston, we have a problem."
print "Success!"
