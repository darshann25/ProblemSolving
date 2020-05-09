# Review the following link for the question prompt: https://www.algoexpert.io/questions/Longest%20Substring%20Without%20Duplication

# O(N) time | O(min(N,A)) space
def longestSubstringWithoutDuplication(string):
    
	maxSubstring = ''
	runningSubstring = ''
	memory = {}
	
	startIdx = 0
	endIdx = 0
	
	for i, newChar in enumerate(string):
		endIdx = i
		if newChar in memory:
			
			startIdx = max(startIdx, memory[newChar] + 1)
		memory[newChar] = endIdx

		runningSubstring = string[startIdx : endIdx + 1]
		
		if len(runningSubstring) >= len(maxSubstring):
			maxSubstring = runningSubstring
	
	return maxSubstring