# Review the following link for the question prompt: https://www.algoexpert.io/questions/Validate%20BST

# O(N) time | O(d) space
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, minVal=float('-inf'), maxVal=float('inf')):
    
	if tree is None:
		return True
	if tree.value < minVal or tree.value >= maxVal:
		return False
	
	leftIsValid = validateBst(tree.left, minVal, tree.value)
	rightIsValid = validateBst(tree.right, tree.value, maxVal)
	
	return leftIsValid and rightIsValid