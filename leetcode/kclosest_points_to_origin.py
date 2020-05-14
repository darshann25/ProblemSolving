# Review the following link for the question prompt: https://leetcode.com/problems/k-closest-points-to-origin/

# O(N + K) time | O(N) space
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        distMemory = {}
        distList = []
        
        for point in points:
            distPoint = math.sqrt((point[0]**2) + (point[1]**2))
            
            if distPoint in distMemory:
                distMemory[distPoint].append(point)
            else:
                distMemory[distPoint] = [point]
                
            distList.append(distPoint)
        
        distList.sort()
        distListCounter = 0
        result = []
        
        while K > 0:
            distListItem = distMemory[distList[distListCounter]]
            
            for point in distListItem:
                if K > 0:
                    result.append(point)
                    K -= 1
            
            distListCounter += 1
            
        return result