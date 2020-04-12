"""
FIND CLOSEST VALUE IN BST
Write a function that takes in a Binary Search Tree (BST) and a target integer
value and returns the closest value to that target value contained in the BST.

You can assume that there will only be one closest value.
"""


# Solution 1 - Traverse and store path
# O(log(n)) time | O(1) space
def findClosestValueInBst(tree, target):
	# Write your code here.
	path = []
	node = tree
	minVal = 9223372036854775807
	closest = -1

	while node:
		if target < node.value:
			val = node.value
			path.append(val)
			node = node.left
		elif target > node.value:
			val = node.value
			path.append(val)
			node = node.right
		else: # target == node.value
			return node.value

		if minVal > abs(val - target):
			minVal = abs(val - target)
			closest = val

	return closest
