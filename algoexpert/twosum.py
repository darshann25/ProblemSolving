"""
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.

"""


# Solution - Brute Force
# Time Complexity - O(n^2)
# Space Complexity - O(1)

# Solution - Sort and search
# Time Complexity - O(n lgn)
# Space Complexity - O(1)

# Solution with hash set - Provides optimal time complexity with some additional space
# Time Complexity : O(n)
# Space Complexity : O(n)
def twoNumberSum(array, targetSum):
    # Write your code here.

	hash = set()

	for num in array:
		if (targetSum - num) in hash:
			return [num, targetSum - num]
		else:
			hash.add(num)

	return []
