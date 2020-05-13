# Review the following link for the question prompt: https://leetcode.com/problems/most-common-word/

# O(N) time | O(N) space
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:        
        
        punctuations = "!?',;."
        
        for char in punctuations:
            paragraph = paragraph.replace(char,' ')

        words = paragraph.split(' ')
        
        memory = {}
        banned = set(banned)
        commonWordFreq = float('-inf')
        commonWord = ''
        
        for word in words:
            word = word.lower()
            
            if word not in banned and word != '':
                if word not in memory:
                    currWordFreq = 1
                else:
                    currWordFreq = memory[word]
                    currWordFreq += 1
                
                memory[word] = currWordFreq
                if commonWordFreq < currWordFreq:
                    commonWordFreq = currWordFreq
                    commonWord = word
                    
        return commonWord