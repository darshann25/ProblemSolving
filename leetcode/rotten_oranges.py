# Review the following link for the question prompt: https://leetcode.com/problems/rotting-oranges/submissions/

# O(N * m) time | O(N) space
import copy
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rottingGrid = copy.deepcopy(grid)
        minutesPassed = 0
        noRotting = False
        
        while not noRotting:
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 2:
                        rottingGrid = self.updateRottingGrid(rottingGrid, row, col)
            # print('rottingGrid: {}'.format(rottingGrid))
            # print('grid: {}'.format(grid))
            minutesPassed += 1
            noRotting = rottingGrid == grid
            grid = copy.deepcopy(rottingGrid)
            
        return minutesPassed-1 if self.allRotten(rottingGrid) else -1
    
    def updateRottingGrid(self, rottingGrid, row, col):
        if row > 0 and rottingGrid[row-1][col] == 1: rottingGrid[row-1][col] = 2
        if row < (len(rottingGrid) - 1) and rottingGrid[row+1][col] == 1: rottingGrid[row+1][col] = 2
        if col > 0 and rottingGrid[row][col-1] == 1: rottingGrid[row][col-1] = 2
        if col < (len(rottingGrid[0]) - 1) and rottingGrid[row][col+1] == 1: rottingGrid[row][col+1] = 2
        
        return rottingGrid
    
    def allRotten(self, grid):
        rotten = True
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                rotten = grid[row][col] != 1
                if not rotten:
                    return False
        return True