# Review the following link for the question prompt: https://leetcode.com/problems/3sum-closest/

# O(N^2) time | O(1) space
class Solution:
    def threeSumClosest(self, array: List[int], targetSum: int) -> int:
        # Write your code here.
        array.sort()
        minTotal = float('inf')
        minDiff = float('inf')
        result = []

        for i in range(len(array) - 2):
            
            l = i + 1
            r = len(array) - 1

            while l < r:
                currTotal = array[i] + array[l] + array[r]
                currResult = [array[i], array[l], array[r]]

                if abs(targetSum - currTotal) <= minDiff:
                    minDiff = abs(targetSum - currTotal)
                    minTotal = currTotal 
                
                if currTotal > targetSum:
                    r -= 1
                elif currTotal < targetSum:
                    l += 1
                else: 
                    break

        return minTotal