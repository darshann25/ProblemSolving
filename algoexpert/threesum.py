"""
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.

"""

# Solution 1 - Brute Force
# Time Complexity - O(n^3)
# Space Complexity - O(1)

# Solution 2 - Sort values and iterate
# Time Complexity - O(n^2)
# Space Complexity - O(n)
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    results = []

    for i in range(len(array) - 2):
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
                l += 1
                r -= 1

    return results
