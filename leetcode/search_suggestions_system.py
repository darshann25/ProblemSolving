# Review the following link for the question prompt: https://leetcode.com/problems/search-suggestions-system/

#O(N + M) time | O(N^2) space
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:                   
        searchMemory = {}
        
        for product in products:
            for idx in range(len(product)):
                searchTerm = product[:idx+1]
                if searchTerm in searchMemory:
                    searchMemory[searchTerm].append(product)
                else:
                    searchMemory[searchTerm] = [product]
        
        suggestions = []
        for idx in range(len(searchWord)):
            searchTerm = searchWord[:idx+1]
            if searchTerm in searchMemory:
                suggestion = searchMemory[searchTerm]
                suggestion.sort()
                suggestions.append(suggestion[:3])
            else:
                suggestions.append([])
        
        return suggestions