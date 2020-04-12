"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1

                else:
                    element = [nums[i],nums[j],nums[k]]
                    res.append(element)

                    while j<k and nums[j]==nums[j+1]:
                        j = j+1
                    while j<k and nums[k]==nums[k-1]:
                        k = k-1

                    j += 1
                    k -= 1

        return res

S = Solution()
solution = [[-1, -1, 2],[-1, 0, 1]]
assert S.threeSum([-1, 0, 1, 2, -1, -4]) == solution, "Houston, we have a problem!"
print("Success!")
