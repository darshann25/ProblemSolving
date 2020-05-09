# Review the following link for the question prompt: https://leetcode.com/problems/string-to-integer-atoi/

# O(N) time | O(1) space
class Solution:
    def myAtoi(self, string: str) -> int:
        
        # pattern = checks for any spaces in the start (optional) | check for +/- sign (optional) | check for all digits in a row
        pattern = "^(\s+)?([-+]?\d+)"   
        allNumbers = re.search(pattern, string)
        
        if allNumbers == None:
            return 0
        else:
            finalNumber = int(float(allNumbers.group()))
            finalNumber = -2 ** 31 if finalNumber < -2 ** 31 else finalNumber
            finalNumber = (2 ** 31 - 1) if finalNumber > 2 ** 31 - 1 else finalNumber
            return finalNumber