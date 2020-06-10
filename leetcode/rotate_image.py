# Review the following link for the question prompt: https://leetcode.com/problems/rotate-image/

# O(n^2) time | O(1) space
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        layers = int(n / 2)
        
        for layer in range(layers):
            for idx in range(layer, n - layer - 1):
                tl = matrix[layer][idx]
                tr = matrix[idx][n-layer-1]
                br = matrix[n-layer-1][n-idx-1]
                bl = matrix[n-idx-1][layer]
                print(tl, tr, br, bl)
                
                tmp = tl
                matrix[layer][idx] = bl
                matrix[n-idx-1][layer] = br
                matrix[n-layer-1][n-idx-1] = tr
                matrix[idx][n-layer-1] = tmp
        
        return matrix