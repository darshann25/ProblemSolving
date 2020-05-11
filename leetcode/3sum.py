# Review the following link for the question prompt: https://leetcode.com/problems/3sum/

# Solution 1 - Brute Force
# Time Complexity - O(n^3)
# Space Complexity - O(1)

# Solution 2 - Sort values and iterate
# Time Complexity - O(n^2)
# Space Complexity - O(n)
class Solution:
    def threeSum(self, array: List[int]) -> List[List[int]]:
        # Write your code here.
        array.sort()
        results = []
        targetSum = 0

        for i in range(len(array) - 2):
            
            if array[i] > targetSum:
                continue
                
            if i > 0 and array[i] == array[i-1]:
                continue
            
            l = i + 1
            r = len(array) - 1

            while l < r:
                total = array[i] + array[l] + array[r]
                result = [array[i], array[l], array[r]]

                if total > targetSum:
                    r -= 1
                elif total < targetSum:
                    l += 1
                else: # total == targetSum
                    results.append(result)
                    
                    while l < r and array[l] == array[l+1]:
                        l += 1
                    while l < r and array[r] == array[r-1]:
                        r -= 1
                        
                    l += 1
                    r -= 1

        return results