# Review the following link for the question prompt: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# O(N) time | O(N) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minLArray = [float('inf')] * len(prices)
        maxRArray = [float('-inf')] * len(prices)
                
        minL = float('inf')
        maxR = float('-inf')
        maxProfit = 0
        idx = 0
        
        while idx < len(prices):
            minL = min(minL, prices[idx])
            minLArray[idx] = minL
            idx += 1
        
        idx -= 1
        while idx >= 0:
            maxR = max(maxR, prices[idx])
            maxRArray[idx] = maxR
            maxProfit = max(maxProfit, maxRArray[idx] - minLArray[idx])
            idx -= 1
        
        return maxProfit