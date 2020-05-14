# Review the following link for the question prompt: https://www.algoexpert.io/questions/Longest%20Palindromic%20Substring

# Without DP -  O(N^2) time | O(1) space
def longestPalindromicSubstringNoDP(string):
    currentLongest = [0,1]
	for i in range(len(string)):
		odd = getLongestPalindrome(string, i-1, i+1)
		even = getLongestPalindrome(string, i-1, i)
		longest = max(odd, even, key = lambda x: x[1] - x[0])
		currentLongest = max(currentLongest, longest, key = lambda x: x[1] - x[0])
	return string[currentLongest[0]: currentLongest[1]]

def getLongestPalindrome(string, startIdx, endIdx):
	while startIdx >= 0 and endIdx < len(string):
		if string[startIdx] != string[endIdx]:
			break
		startIdx -= 1
		endIdx += 1
	return [startIdx + 1, endIdx]

# With DP - O(N^2) time | O(N^2) space
def longestPalindromicSubstring(string):
    
	if not string: return string
	
	strLen = len(string)
	dp = [[0] * strLen for i in range(strLen)]
	pallindrome = string[0]
	pallindromeLen = 1
	
	for i in range(strLen):
		dp[i][i] = 1
	
	for length in range(2, strLen + 1):
		for i in range(strLen - length + 1):
			j = i + length - 1
			
			if string[i] == string[j]:
				if abs(i - j) == 1 or dp[i+1][j-1] == 1:
					dp[i][j] = 1
					pallindrome = string[i:j+1]
					pallindromeLen = length
					continue
			dp[i][j] = 0
	
	return pallindrome