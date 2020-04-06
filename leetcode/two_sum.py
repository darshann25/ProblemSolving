# coding=utf-8
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # init dictionary to store historic values
        numsDict = {}
        
        # iterate over values in list
        for index in range(len(nums)):
            
            # get current value
            value = nums[index]

            # check if target - value in stored values
            if (target - value) in numsDict.keys():
                return [numsDict[target - value], index]
            
            # add value to dictionary
            numsDict[value] = index

s = Solution()
nums = [2, 7, 11, 15]
assert s.twoSum(nums, 9) == [0,1], "Houston, we have a problem!"
print("Success!")

# Time Complexity : O(n)
# Space Complexity : O(1)
