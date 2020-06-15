# Review the following link for the question prompt: https://leetcode.com/problems/find-median-from-data-stream/

# Insert - O(log N) time | Find Median - O(1) time | O(N) space
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if len(self.lower) == 0:
            heapq.heappush(self.lower, -num)
            return
        
        if num <= - self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)
        
        if len(self.upper) - len(self.lower) == 2:
            heapq.heappush(self.lower, - heapq.heappop(self.upper))
        elif len(self.lower) - len(self.upper) == 2:
            heapq.heappush(self.upper, - heapq.heappop(self.lower))
        
        
        
    def findMedian(self) -> float:
        if len(self.lower) == len(self.upper):
            return ((- self.lower[0] + self.upper[0]) / 2.0)
        elif len(self.lower) > len(self.upper):
            return - self.lower[0]
        else:
            return self.upper[0]

#####################################################

# Insert - O(1) time | Find Median - O(N logN) time | O(N) space
# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.list = []

#     def addNum(self, num: int) -> None:
#         self.list.append(num)

#     def findMedian(self) -> float:
#         self.list.sort()
#         listLen = len(self.list)
#         if len(self.list) % 2 == 0:
#             return (self.list[int(listLen/2)] + self.list[int(listLen/2)-1]) / 2.0
#         else:
#             return self.list[int(listLen/2)]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()