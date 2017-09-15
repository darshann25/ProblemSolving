"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Given n = 3,

You should return the following matrix:
 [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]
 """

import math

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        n = 1

        matrix = [[0]*A for j in xrange(A)]

        rowMax = A - 1
        rowMin = 0
        colMax = A - 1
        colMin = 0

        row = 0
        col = 0

        while n <= math.pow(A, 2):
            while col <= colMax:
                matrix[row][col] = n
                n += 1
                col += 1
            rowMin += 1
            row +=1
            col -=1

            while row <= rowMax:
                matrix[row][col] = n
                n += 1
                row += 1
            colMax -= 1
            col -= 1
            row -= 1

            while col >= colMin:
                matrix[row][col] = n
                n += 1
                col -= 1
            rowMax -= 1
            row -= 1
            col += 1

            while row >= rowMin:
                matrix[row][col] = n
                n += 1
                row -= 1
            colMin += 1
            col += 1
            row += 1

        return matrix


s = Solution()
result = [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
assert s.generateMatrix(5) == result , "Houston, we have a problem"
print "Success!"
