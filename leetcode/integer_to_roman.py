# Review the following link for the question prompt: https://leetcode.com/problems/integer-to-roman/

# O(N) time | O(1) space
class Solution:
    def intToRoman(self, num: int) -> str:
        
        mapping = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', \
                   400:'CD', 500:'D', 900:'CM', 1000:'M'}
        
#        # Code to create subtractions of smaller numbers from larger numbers
#         mapping_list = [1, 5, 10, 50, 100, 500, 1000]
#         for i in range(len(mapping_list) - 1):
#             for j in range(i+1, len(mapping_list)):
                
#                 smallerNum = mapping_list[i]
#                 largerNum = mapping_list[j]
#                 if largerNum - smallerNum not in mapping:
#                     mapping[largerNum - smallerNum] = mapping[smallerNum] + mapping[largerNum]
                
        mapping_list = list(mapping.keys())
        mapping_list.sort(reverse=True)

        roman = []
        
        while num != 0:
            for divisor in mapping_list:
                quotient = int(num / divisor)
                remainder = num % divisor
                # print(quotient, remainder)
                
                if quotient > 0:
                    roman.append(quotient * mapping[divisor])
                    num = remainder
                if num == 0:
                    break
                # print(roman)
        
        return ''.join(roman)