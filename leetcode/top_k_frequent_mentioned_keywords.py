# Review the following link for the question prompt: https://leetcode.com/discuss/interview-question/542597/

# O(N + nlog(n)) time | O(n) space
class Solution:
    def topKFrequentKeywords(self, k, keywords, reviews):
        
        keywordMemory = {}
        keywords = set(keywords)

        for review in reviews:
            words = set(review.lower().replace('[^a-zA-Z0-9]','').split())
            for word in words:
                if word in keywords:
                    if word in keywordMemory:
                        currFreq = keywordMemory[word]
                        currFreq[1] += 1
                        keywordMemory[word] = currFreq
                    else:
                        currFreq = [word, 1]
                        keywordMemory[word] = currFreq
        
        wordFreq = keywordMemory.values()
        wordFreq.sort(reverse = True, key = lambda x : x[1])
        wordFreq = [x[0] for x in wordFreq]
        return wordFreq[:k] if k <= len(wordFreq) else wordFreq

s = Solution()
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]
expected_output = ["anacell", "betacellular"]
print('\nExample 1 :\nOutput: {}\nExpected Output: {}'.format(s.topKFrequentKeywords(k, keywords, reviews), expected_output))

k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
expected_output = ["betacellular", "anacell"]
print('\nExample 2 :\nOutput: {}\nExpected Output: {}'.format(s.topKFrequentKeywords(k, keywords, reviews), expected_output))