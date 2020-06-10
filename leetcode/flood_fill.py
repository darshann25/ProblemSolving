# Review the following link for the question prompt: https://leetcode.com/problems/flood-fill/

# O(N) time | O(N) space
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = [(sr, sc)]
        visited = [[False for x in range(len(image[0]))] for y in range(len(image))]
        oldColor = image[sr][sc]

        while queue:
            currRow, currCol = queue.pop(0)
            image[currRow][currCol] = newColor
            visited[currRow][currCol] = True
            
            for step in [[1,0],[0,1],[-1,0],[0,-1]]:
                newRow = currRow + step[0]
                newCol = currCol + step[1]
                if newRow >= 0 and newRow < len(image) and newCol >= 0 and newCol < len(image[0]) and not visited[newRow][newCol] and image[newRow][newCol] == oldColor:
                    queue.append((newRow,newCol))
        
        return image