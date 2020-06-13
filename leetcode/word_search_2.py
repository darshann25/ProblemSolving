# Review the following link for the question prompt: https://leetcode.com/problems/word-search-ii/

# O(w*n^2) time | O(w) space
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

    def search(self, word):
        node = self.root
        for char in word:
            node = node.children[c]
            if not node:
                return False
        return node.isWord

class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result, trie = [], Trie()
        node = trie.root
        
        for word in words:
            trie.insert(word)
            
        for rowIdx in range(len(board)):
            for colIdx in range(len(board[0])):
                self.searchBoardDFS(board, node, rowIdx, colIdx, '', result)
        
        return result
    
    def searchBoardDFS(self, board, node, rowIdx, colIdx, path, result):
        if node.isWord:
            result.append(path)
            node.isWord = False
        
        if rowIdx < 0 or rowIdx >= len(board) or colIdx < 0 or colIdx >= len(board[0]):
            return
        
        temp = board[rowIdx][colIdx]
        if temp not in node.children:
            return
        
        board[rowIdx][colIdx] = '#'
        for newRowIdx, newColIdx in [(rowIdx-1,colIdx),(rowIdx+1,colIdx),(rowIdx,colIdx-1),(rowIdx,colIdx+1)]:
            self.searchBoardDFS(board, node.children[temp], newRowIdx, newColIdx, path+temp, result)
        board[rowIdx][colIdx] = temp
        
        return result
    
#################################################
    
    def findWordsWithoutTrie(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        
        for word in words:
            if self.exist(board, word):
                result.append(word)
        return result
    
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