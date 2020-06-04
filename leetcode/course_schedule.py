# Review the following link for the question prompt: https://leetcode.com/problems/course-schedule/submissions/

# O(N) time | O(N+N) space
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # counter
        counter = 0
        
        # calculate number of in-degrees coming into the graph
        inDegree = [0] * numCourses
        origins = {}
        for idx in range(len(prerequisites)):
            inDegree[prerequisites[idx][0]] += 1
            
            if prerequisites[idx][1] in origins:
                origins[prerequisites[idx][1]].append(prerequisites[idx])
            else:
                origins[prerequisites[idx][1]] = [prerequisites[idx]]
        
        # create and update stack with nodes that have no edges coming in (in-degree = 0)
        stack = []
        for idx in range(len(inDegree)):
            if inDegree[idx] == 0:
                stack.append(idx)
        
        # DFS using the stack and update the counter
        while stack:
            curr = stack.pop(0)
            counter += 1
            
            if curr in origins:
                prereqs = origins[curr]
                for prereq in prereqs:
                    inDegree[prereq[0]] -= 1
                    if inDegree[prereq[0]] == 0:
                        stack.append(prereq[0])
            
        return counter == numCourses

# O(N^N) time | O(N) space
#     def canFinishSlow(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
#         # counter
#         counter = 0
        
#         # calculate number of in-degrees coming into the graph
#         inDegree = [0] * numCourses
#         for idx in range(len(prerequisites)):
#             inDegree[prerequisites[idx][0]] += 1
        
#         # create and update stack with nodes that have no edges coming in (in-degree = 0)
#         stack = []
#         for idx in range(len(inDegree)):
#             if inDegree[idx] == 0:
#                 stack.append(idx)
        
#         # DFS using the stack and update the counter
#         while stack:
#             curr = stack.pop(0)
#             counter += 1
            
#             for idx in range(len(prerequisites)):
#                 if prerequisites[idx][1] == curr:
#                     inDegree[prerequisites[idx][0]] -= 1
#                     if inDegree[prerequisites[idx][0]] == 0:
#                         stack.append(prerequisites[idx][0])
        
#         return counter == numCourses