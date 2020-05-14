# Review the following link for the question prompt: https://leetcode.com/problems/kth-largest-element-in-a-stream/

# O(N log(N)) time | O(1) space
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]