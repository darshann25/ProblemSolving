# Review the following link for the question prompt: https://leetcode.com/problems/missing-number/

# O(N) time | O(1) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = int(n*(n+1)/2)
        return total - sum(nums)