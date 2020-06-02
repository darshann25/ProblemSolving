# Review the following link for the question prompt: https://leetcode.com/problems/product-of-array-except-self/

# O(N) time | O(1) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        prod = 1
        for idx in range(len(nums)):
            result[idx] *= prod
            prod *= nums[idx]
        
        prod = 1
        for idx in range(len(nums)-1, -1, -1):
            result[idx] *= prod
            prod *= nums[idx]
        
        return result