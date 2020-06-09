# Review the following link for the question prompt: https://leetcode.com/problems/merge-intervals/

# O(n logn + n^2) time | O(n) space
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        resultIntervals = []
        idx = 0
        
        while idx < len(intervals):
            interval = intervals[idx]
            lowerLimit = interval[0]
            upperLimit = interval[1]
            
            for innerIdx in range(idx+1, len(intervals)):
                innerInterval = intervals[innerIdx]
                if innerInterval[0] <= upperLimit:
                    upperLimit = innerInterval[1] if innerInterval[1] > upperLimit else upperLimit
                    if idx != len(intervals) - 1: idx += 1
                else:
                    break
            
            resultIntervals.append([lowerLimit, upperLimit])
            idx += 1
        
        return resultIntervals