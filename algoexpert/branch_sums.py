# Review the following link for the question prompt:https://www.algoexpert.io/questions/Branch%20Sums

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time Complexity: O(N)
# Space Complexity: O(N)
def branchSums(root, currSum=0):
    # Write your code here.
    
	currSum += root.value
	if root.left == None and root.right == None:
		return [currSum]
	
	sums = []
	if root.left: sums += branchSums(root.left, currSum)
	if root.right: sums += branchSums(root.right, currSum)
	
	return sums