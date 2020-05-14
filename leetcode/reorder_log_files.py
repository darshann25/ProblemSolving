# Review the following link for the question prompt: https://leetcode.com/problems/reorder-data-in-log-files/

# O(N + nlog(n)) time | O(N) space
class Solution:
    def letterLogFunc(self, l):
        strL = l.split(' ')
        strL.append(strL[0])
        return strL[1:]
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letterLogs = []
        digitLogs = []
        
        for log in logs:
            if log.split(' ')[1].isnumeric():
                digitLogs.append(log)
            else:
                letterLogs.append(log)
        
        letterLogs.sort(key=self.letterLogFunc)
        return letterLogs + digitLogs