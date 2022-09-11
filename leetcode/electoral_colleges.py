# Question from CS6515 - HW1 

# O(n*Z) time | O(n*Z) space
class Solution():
    def electoral_colleges(self, P, V, Z):
        
        rows = len(P)
        cols = Z + 1
        T = [[0 for _ in range(cols)] for _ in range(rows)]
        for z in range(1, cols):
            T[0][z] = float('inf')
        for i in range(rows):
            T[i][0] = 0
        
        for i in range(1, rows):
            for z in range(1, cols):
                if V[i] <= z:
                    t = min(T[i-1][(z-V[i]):])
                    T[i][z] = min(P[i] + t, T[i-1][z])
                else:
                    T[i][z] = T[i-1][z]
        
        print(T[3][2])
        print(T)
        return T[len(P)-1][Z]

S = Solution()
P = [0, 200,100,30,700,250]
V = [0, 5, 1, 2, 7, 6]
Z = 12
print(S.electoral_colleges(P,V,Z))
# result = 480