"""
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:
Input:
1 2 3
4 5 6
7 8 9

Return the following :
[
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]

Input :
1 2
3 4

Return the following  :
[
  [1],
  [2, 3],
  [4]
]
"""

class Solution:
    # @param a : list of list of integers
    # @return a list of list of integers
    def diagonal(self, a):
        l = len(a)
        result = [[] for x in range(2 * l - 1)]
        for r in range(l):
            for c in range(l):
                result[r + c].append(a[r][c])

        return result

s = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result_expected = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
assert s.diagonal(matrix) == result_expected, "Houston, we have a problem!"
print "Success!"



