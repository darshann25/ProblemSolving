# coding=utf-8
"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture

Example:


Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d]

If a < c OR a==c AND b < d.
"""


class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, num):
        first = 2
        second = 0

        while first < num:
            second = num - first

            if self.isPrimeAlt(first) and self.isPrimeAlt(second):
                break
            first += 1
        return [first, second]

    # O(n)
    def isPrime(self, num):
        if num == 2: return True
        if num % 2 == 0: return False

        i = 3
        while i < num:
            if num % i == 0: return False
            i += 2
        return True

    # O(1)
    def isPrimeAlt(self, num):
        if num == 2: return True
        if num % 2 == 0: return False

        return pow(2, num - 1, num) == 1


s = Solution()
assert s.primesum(4) == [2, 2], "Houston, we have a problem!"
print "Success!"
