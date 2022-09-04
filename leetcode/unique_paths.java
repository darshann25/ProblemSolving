// Review the following link for the question prompt: https://leetcode.com/problems/unique-paths

// O(m*n) time | O(m*n) space
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] T = new int[m][n];
        
        // handle for base case
        T[m-1][n-1] = 0;
        
        for (int i = 0; i < m; i++) T[i][n-1] = 1;
        for (int j = 0; j < n; j++) T[m-1][j] = 1;
                
        // recurrence
        for (int i = m-2; i >= 0; i--) {
            for (int j = n-2; j >= 0; j--) {
                T[i][j] = T[i+1][j] + T[i][j+1];
            }
        }
        
        return T[0][0];
    }
}