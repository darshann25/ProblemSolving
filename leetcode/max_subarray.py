# Review the following link for the question prompt: https://leetcode.com/problems/maximum-subarray/

# O(N) time | O(1) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningSum = 0
        maxSum = float('-inf')
        
        for num in nums:
            runningSum += num
            maxSum = max(maxSum, runningSum)
            runningSum = runningSum if runningSum > 0 else 0
            
        return maxSum