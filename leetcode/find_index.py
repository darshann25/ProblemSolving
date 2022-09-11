# Question from CS6515 - HW2
import math

# O(lg(n)) time | O(lg(n)) space
class Solution():
    def find_index(self, A, lower_idx):
        n = len(A)
        i = math.ceil(int(n/2)) # 3
        v = (2* (i + lower_idx)) + 5 # 11
        # print(A, n, (i+lower_idx), v, A[i])

        if n <= 0:
            # print(n)
            return False
        if v == A[i]:
            # print(v, A[i])
            return True
        if n != 1:
            if v < A[i]:
                return self.find_index(A[:i], lower_idx)
            else: # if v > A[i]:
                return self.find_index(A[i:], i+1)
        return False        


S = Solution()
A = [5, 7, 9, 13]
s = [7, 9, 11, 13]
print(S.find_index(A, 1))
# result = True

test_cases = {
    1: {"array": [-1, 1]},
    2: {"array": [1, 9]},
    3: {"array": [1, 1001]},
    4: {"array": [1, 3, 5, 7]},
    5: {"array": [-1, -3, -5, -7]},
    6: {"array": [7, 9, 11, 13]},
    7: {"array": [3, 9, 13, 17]},
    8: {"array": [-3, 3, 11, 17]},
    9: {"array": [-11, 1, 3, 13]},
} 

for k,v in test_cases.items():
    print(str(k) + " : " + str(S.find_index(v["array"], 1)))