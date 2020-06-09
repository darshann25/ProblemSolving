# Review the following link for the question prompt: https://leetcode.com/problems/merge-intervals/

# O(n logn) time | O(n) space
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals: return intervals
        
        intervals.sort(key = lambda x : x[0])
        resultIntervals = []
        # idx = 0
        
        lowerLimit = intervals[0][0]
        upperLimit = intervals[0][1]
        
        for idx in range(1, len(intervals)):
            if intervals[idx][0] >= lowerLimit and intervals[idx][0] <= upperLimit:
                upperLimit = max(intervals[idx][1], upperLimit)
            else:
                resultIntervals.append([lowerLimit, upperLimit])
                lowerLimit = intervals[idx][0]
                upperLimit = intervals[idx][1]
        
        resultIntervals.append([lowerLimit, upperLimit])
        
        return resultIntervals