# Review the following link for the question prompt: https://www.algoexpert.io/questions/Group%20Anagrams

# O(N + N * mlog(m)) time | O(N) space
def groupAnagrams(words):
    memory = {}
	for anagram in words:
		sorted_anagram = ''.join(sorted(anagram))
		if sorted_anagram in memory:
			memory[sorted_anagram].append(anagram)
		else:
			memory[sorted_anagram] = [anagram]

	results = []
	for value in memory.values():
		results.append(value)

	return results
