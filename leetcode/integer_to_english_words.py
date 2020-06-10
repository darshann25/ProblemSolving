# Review the following link for the question prompt: https://leetcode.com/problems/integer-to-english-words/

# O(N) time | O(1) space
class Solution:
    def numberToWords(self, num: int) -> str:
        
        if num == 0: return 'Zero'
        
        numbers = [0 for x in range(4)]
        idx = 0
        while num != 0:
            numbers[idx] = (num % 1000)
            num = int(num / 1000)
            idx += 1
        
        hundredsNum, thousandsNum, millionsNum, billionsNum = numbers
        
        result = ''
        if billionsNum != 0:
            result += ' ' + self.convertThreeNumbersToWords(billionsNum) + ' Billion'
        if millionsNum != 0:
            result += ' ' + self.convertThreeNumbersToWords(millionsNum) + ' Million'
        if thousandsNum != 0:
            result += ' ' + self.convertThreeNumbersToWords(thousandsNum) + ' Thousand'
        if hundredsNum != 0:
            result += ' ' + self.convertThreeNumbersToWords(hundredsNum)
        
        return result[1:]    
        
        
    def convertThreeNumbersToWords(self, num):
        units = [None,'One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        teens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        tens = [None,None,'Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        
        unitsPlace = num % 10
        tensPlace = int(num / 10) % 10
        hundredsPlace = int(num / 100) % 10
        
        result = ''
        if hundredsPlace > 0:
            result += ' ' + units[hundredsPlace] + ' Hundred'
        if tensPlace == 1:
            result += ' ' + teens[unitsPlace]
            return result[1:]
        if tensPlace != 0:
            result += ' ' + tens[tensPlace]
        if unitsPlace != 0:
            result += ' ' + units[unitsPlace]
        
        return result[1:]