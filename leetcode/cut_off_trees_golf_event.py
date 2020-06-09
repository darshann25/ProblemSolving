# Review the following link for the question prompt: https://leetcode.com/problems/cut-off-trees-for-golf-event/

# O(nlogn + m) time | O(n+m) space, where n is size of forest, m is non-zero trees
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        trees = []
        for r in range(len(forest)):
            for c in range(len(forest[0])):
                h = forest[r][c]
                if h > 1 : trees.append([h, r, c])
        trees.sort(key = lambda x : x[0])
        
        minDist = 0
        startRow = 0
        startCol = 0
        
        for idx in range(len(trees)):
            endRow = trees[idx][1]
            endCol = trees[idx][2]
            dist = self.getMinDistance(forest, startRow, startCol, endRow, endCol)
            if dist == -1:
                return -1
            minDist += dist
            startRow = endRow
            startCol = endCol
        return minDist
    
    def getMinDistance(self, forest, startRow, startCol, endRow, endCol):
        # TODO: Implement BFS
        visited = [[False for i in range(len(forest[0]))] for n in range(len(forest))]
        queue = [(startRow, startCol, 0)]
        dist = 0
        visited[startRow][startCol] = True
        
        while queue:
            newPos = queue.pop(0)
            newRow = newPos[0]
            newCol = newPos[1]
            
            if newRow == endRow and newCol == endCol:
                return newPos[2]
            
            for direction in [[0,-1],[-1,0],[0,1],[1,0]]:
                currRow = newRow + direction[0]
                currCol = newCol + direction[1]
                
                if currRow >= 0 and currRow < len(forest) and currCol >= 0 and currCol < len(forest[0]) and forest[currRow][currCol] != 0 and not visited[currRow][currCol]:
                    visited[currRow][currCol] = True
                    queue.append([currRow, currCol, newPos[2]+1])
                    
        return -1