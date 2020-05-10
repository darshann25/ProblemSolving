# Review the following link for the question prompt: https://leetcode.com/problems/container-with-most-water/

class Solution:
    # O(N) time | O(1) space
    def maxArea(self, height: List[int]) -> int:
        maxWaterContainer = 0
        runningWaterContainer = 0
        leftIdx = 0
        rightIdx = len(height) - 1
        
        while leftIdx < rightIdx:
            leftPartition = height[leftIdx]
            rightPartition = height[rightIdx]
            htContainer = min(leftPartition, rightPartition)
            wdContainer = (rightIdx - leftIdx)
            runningWaterContainer =  htContainer * wdContainer
            maxWaterContainer = max(maxWaterContainer, runningWaterContainer)
            
            if leftPartition <= rightPartition:
                leftIdx += 1
            else:
                rightIdx -= 1
        
        return maxWaterContainer
        
    # O(N^2) time | O(1) space
    def maxAreaSlow(self, height: List[int]) -> int:
        maxWaterContainer = 0
        runningWaterContainer = 0
        
        for leftIdx in range(len(height) - 1):
                for rightIdx in range(leftIdx + 1, len(height)):
                    
                    leftPartition = height[leftIdx]
                    rightPartition = height[rightIdx]
                    
                    htContainer = min(leftPartition, rightPartition)
                    wdContainer = (rightIdx - leftIdx)
                    
                    runningWaterContainer =  htContainer * wdContainer
                    maxWaterContainer = max(maxWaterContainer, runningWaterContainer)
        return maxWaterContainer