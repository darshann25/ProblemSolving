# Review the following link for the question prompt: https://www.algoexpert.io/questions/Subarray%20Sort

# Time Complexity: O(N)
# Space Complexity: O(1)
def subarraySort(array):
    
	minOutOfOrder = float('inf')
	maxOutOfOrder = float('-inf')
	
	for i, num in enumerate(array):
		if isOutOfOrder(i, num, array):
			minOutOfOrder = min(minOutOfOrder, num)
			maxOutOfOrder = max(maxOutOfOrder, num)
	if minOutOfOrder == float('inf'):
		return [-1, -1]
	
	subarrayLeftIdx = 0
	while minOutOfOrder >= array[subarrayLeftIdx]:
		subarrayLeftIdx += 1
	
	subarrayRightIdx = len(array) - 1
	while maxOutOfOrder <= array[subarrayRightIdx]:
		subarrayRightIdx -= 1
	return [subarrayLeftIdx, subarrayRightIdx]

def isOutOfOrder(i, num, array):
	if i == 0:
		return num > array[i+1]
	if i == len(array) - 1:
		return num < array[i-1]
	return num > array[i+1] or num < array[i-1]
						