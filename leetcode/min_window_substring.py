# Review the following link for the question prompt: https://leetcode.com/problems/minimum-window-substring/

# O(M + N) time | O(M + N) space
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t or len(t) > len(s):
            return ""
        
        filtered_S = []
        minWindow = float('inf')
        minSubstring = ""
        slowPtr = 0
        fastPtr = 0
        t_memory = Counter(t)
        window_memory = {}
        required = len(t_memory)
        formed = 0
        
        for idx, char in enumerate(s):
            if char in t_memory:
                filtered_S.append((idx,char))
                window_memory[char] = 0
        
        if not filtered_S:
            return ""
        
        slowStrChar = filtered_S[slowPtr][1]
        window_memory[slowStrChar] += 1
        if window_memory[slowStrChar] == t_memory[slowStrChar]:
            formed += 1        
        
        while slowPtr <= len(filtered_S) - 1:
            
            slowStrPtr = filtered_S[slowPtr][0]
            fastStrPtr = filtered_S[fastPtr][0]
            candidateSubstring = s[slowStrPtr:fastStrPtr+1]
            
            if formed == required:
                if minWindow > len(candidateSubstring):
                    minWindow = len(candidateSubstring)
                    minSubstring = candidateSubstring
                window_memory[slowStrChar] -= 1
                if window_memory[slowStrChar] < t_memory[slowStrChar]:
                    formed -= 1
                
                slowPtr += 1
                slowStrChar = filtered_S[slowPtr][1] if slowPtr <= len(filtered_S) - 1 else ""
            elif fastPtr < len(filtered_S) - 1: 
                fastPtr += 1
                fastStrChar = filtered_S[fastPtr][1]
                window_memory[fastStrChar] += 1
                if window_memory[fastStrChar] == t_memory[fastStrChar]:
                    formed += 1
            else:
                window_memory[slowStrChar] -= 1
                if window_memory[slowStrChar] < t_memory[slowStrChar]:
                    formed -= 1
                
                slowPtr += 1
                slowStrChar = filtered_S[slowPtr][1] if slowPtr <= len(filtered_S) - 1 else ""
                
        return minSubstring
    
#     def minWindowSlow(self, s: str, t: str) -> str:
        
#         if len(s) < len(t):
#             return ""
        
#         print(len(s))
#         print(len(t))
        
#         minWindow = float('inf')
#         minSubstring = ""
#         slowPtr = 0
#         fastPtr = 1
#         t_memory = {}
        
#         for char in t:
#             if char in t_memory:
#                 t_memory[char] += 1
#             else:
#                 t_memory[char] = 1
        
#         while slowPtr < len(s):
#             candidateSubstring = s[slowPtr:fastPtr]
#             # print(candidateSubstring)
#             # print(t_memory)

#             if self.isSubstring(candidateSubstring,t_memory):
#                 if minWindow > len(candidateSubstring):
#                     minWindow = len(candidateSubstring)
#                     minSubstring = candidateSubstring
#                 slowPtr += 1
#             elif fastPtr > len(s): 
#                 slowPtr += 1
#             else:
#                 fastPtr += 1
        
#         return minSubstring
            
#     def isSubstring(self, s, t):
        
#         t_memory = t.copy()
        
#         for char in s:
#             if char in t_memory:
#                 t_memory[char] -= 1
        
#         for v in t_memory.values():
#             # print(v)
#             if v > 0:
#                 return False
#         return True                
            