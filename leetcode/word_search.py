# Review the following link for the question prompt: https://leetcode.com/problems/word-search/

# O(N^2) time | O(w) space
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for rowIdx in range(len(board)):
            for colIdx in range(len(board[0])):
                # print(rowIdx, colIdx)
                if board[rowIdx][colIdx] == word[0]:
                    if self.searchBoard(word, 0, board, rowIdx, colIdx):
                        return True
        return False
    
    def searchBoard(self, word, wordIdx, board, rowIdx, colIdx):
        if wordIdx == len(word):
            return True
        
        if rowIdx < 0 or rowIdx >= len(board) or colIdx < 0 or colIdx >= len(board[0]) or board[rowIdx][colIdx] != word[wordIdx]:
            return False
        
        temp = board[rowIdx][colIdx]
        board[rowIdx][colIdx] = '#'
        
        found = self.searchBoard(word, wordIdx+1, board, rowIdx-1, colIdx) or \
                    self.searchBoard(word, wordIdx+1, board, rowIdx+1, colIdx) or \
                    self.searchBoard(word, wordIdx+1, board, rowIdx, colIdx-1) or \
                    self.searchBoard(word, wordIdx+1, board, rowIdx, colIdx+1)
        
        board[rowIdx][colIdx] = temp
        return found