"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def trap(self, height):

        if not height:
            return 0

        water = 0
        i = len(height)
        right = [0] * i
        left = [0] * i

        maxR = height[i - 1]
        maxL = height[0]

        while i > 0:

            if height[i-1] > maxR:
                maxR = height[i-1]

            right[i-1] = maxR
            i -= 1

        while i < len(height):

            if height[i] > maxL:
                maxL = height[i]

            left[i] = maxL
            water += min(left[i], right[i]) - height[i]
            i += 1

        return water

s = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
assert s.trap(height) == 6, "Houston, we have a problem!"
print("Success!")
