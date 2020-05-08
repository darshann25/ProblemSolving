# Review the following link for the question prompt: https://www.algoexpert.io/questions/Branch%20Sums

# Time Complexity: O(N^2 + m)
# Space Complexity: O(N + m)
def patternMatcher(pattern, string):
    
	if len(string) < len(pattern):
		return []
	
	newPattern = getNewPattern(pattern)
	didSwitch = pattern[0] == 'y'
	firstYPos, counts = getCountsAndFirstYPos(newPattern)
		
	if counts['y'] != 0:
		for lenOfX in range(1, len(string)):
			lenOfY = (len(string) - (lenOfX * counts['x'])) / counts['y']
			if lenOfY % 1 != 0:
				continue
			lenOfY = int(lenOfY)
			idxOfY = firstYPos * lenOfX
			x = string[:lenOfX]
			y = string[idxOfY: idxOfY + lenOfY]
			potentialMatch = map(lambda char: x if char == 'x' else y, newPattern)
			
			if string == ''.join(potentialMatch):
				return [x, y] if not didSwitch else [y, x]
	else:
		lenOfX = len(string) / counts['x']
		if lenOfX % 1 == 0:
			lenOfX = int(lenOfX)
			x = string[:lenOfX]
			y = ''
			potentialMatch = map(lambda char: x if char == 'x' else y, newPattern)
			if string == ''.join(potentialMatch):
				return [x, y] if not didSwitch else [y, x]
	return []

def getNewPattern(pattern):
	patternLetters = list(pattern)
	
	if patternLetters[0] == 'x':
		return patternLetters
	else:
		return list(map(lambda char: 'x' if char == 'y' else 'y', patternLetters))
	
def getCountsAndFirstYPos(pattern):
	counts = {'x':0, 'y':0}
	firstYPos = None
	
	for index, char in enumerate(pattern):
		if char == 'y' and firstYPos is None:
			firstYPos = index
		counts[char] += 1
	
	return firstYPos, counts
