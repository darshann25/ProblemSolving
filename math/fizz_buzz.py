# coding=utf-8
"""
Given a positive integer N, print all the integers from 1 to N. But for multiples of 3 print “Fizz” instead
of the number and for the multiples of 5 print “Buzz”. Also for number which are multiple of 3 and 5, prints “FizzBuzz”.

Example

N = 5
Return: [1 2 Fizz 4 Buzz]
Note: Instead of printing the answer, you have to return it as list of strings.
"""


class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        result = []

        for i in range(A):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                result.append("FizzBuzz")
            elif (i + 1) % 3 == 0:
                result.append("Fizz")
            elif (i + 1) % 5 == 0:
                result.append("Buzz")
            else:
                result.append(i + 1)

        return result


s = Solution()
exp_result = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
assert s.fizzBuzz(15) == exp_result, "Houston, we have a problem"
print "Success!"
