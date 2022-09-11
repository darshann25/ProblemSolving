# Question from CS6515 - HW2 

# O(n^n) time | O(n) space
class Solution():
    def road_trip(self, P, C, M=300):

        n = len(P) - 1
        T = [0 for _ in range(n+1)]

        # base cases
        P[0] = 0
        C[0] = 0
        T[0] = 0

        j = 0
        
        for i in range(1, n + 1):
            # print(i, j)
            # print(P)
            # print(C)
            # print(T)
            while C[j] < C[i] - M and j <= i:
                j += 1
            #     print(i, j)
            # print(T[j:i+1])
            T[i] = min(T[j:i]) + P[i]
        
        print(T)
        return T[n]

        

S = Solution()
P = [0, 12, 2, 20, 3, 12, 2, 20, 3]
C = [0, 100, 100, 250, 400, 500, 650, 700, 950]
M = 300
print(S.road_trip(P,C,M))
# result = 10

P = [0, 12, 20, 3]
C = [0, 100, 250, 400]
M = 300
print(S.road_trip(P,C,M))
# result = 15