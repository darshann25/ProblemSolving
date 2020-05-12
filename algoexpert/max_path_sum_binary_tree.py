# Review the following link for the question prompt: https://www.algoexpert.io/questions/Max%20Path%20Sum%20In%20Binary%20Tree

# O(N) time | O(log(N)) space
def maxPathSum(tree):
	_, maxPathSum = findMaxSum(tree)
	return maxPathSum
	

def findMaxSum(node):
	if node is None:
		return (0,float('-inf'))
	
	leftMaxSumAsBranch, leftMaxSum = findMaxSum(node.left)
	rightMaxSumAsBranch, rightMaxSum = findMaxSum(node.right)
	
	maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
	maxSumAsBranch = max(maxChildSumAsBranch + node.value, node.value)
	maxSumAsRootNode = max(leftMaxSumAsBranch + node.value + rightMaxSumAsBranch, maxSumAsBranch)
	maxPathSum = max(leftMaxSum, rightMaxSum, maxSumAsRootNode)
	
	return maxSumAsBranch, maxPathSum