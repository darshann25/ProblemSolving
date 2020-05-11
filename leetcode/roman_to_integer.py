# Review the following link for the question prompt: https://leetcode.com/problems/roman-to-integer/

# O(N) time | O(1) space
class Solution:
    def romanToInt(self, roman: str) -> int:
        mapping = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, \
                   'CD':400, 'D':500, 'CM':900, 'M':1000}
        integer = 0
        idx = 0
        
        while idx < len(roman):
            char = roman[idx]
            
            if idx + 1 < len(roman):
                doubleChar = roman[idx:idx+2]
                
                if doubleChar in mapping:
                    integer += mapping[doubleChar]
                    idx += 2
                    continue
                
            if char in mapping:
                integer += mapping[char]
                idx += 1
                    
        return integer