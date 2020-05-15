# Review the following link for the question prompt: https://leetcode.com/problems/critical-connections-in-a-network/

# O(E+V) time | O(E) space
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        self.time = 0
        self.visitedTimes = [float('inf')] * n
        self.lowTimes = [float('inf')] * n
        self.visited = [False] * n
        self.criticalConnections = []
        
        graph = self.buildGraph(connections)
        self.dfs(graph, 0, -1)
        return self.criticalConnections
        
        
    def buildGraph(self, connections):
        graph = {}
        for edge in connections:
            a = edge[0]
            b = edge[1]
            
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]
                
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]
        
        return graph
    
    def dfs(self, graph, currNode, parentNode):
        self.visited[currNode] = True
        self.visitedTimes[currNode] = self.lowTimes[currNode] = self.time
        self.time += 1
        
        for neighbor in graph[currNode]:
            if neighbor == parentNode: continue
            if not self.visited[neighbor]:
                self.dfs(graph, neighbor, currNode)
                
                self.lowTimes[currNode] = min(self.lowTimes[currNode], self.lowTimes[neighbor])
                if self.visitedTimes[currNode] < self.lowTimes[neighbor]:
                    self.criticalConnections.append([currNode, neighbor])
            else:
                self.lowTimes[currNode] = min(self.lowTimes[currNode], self.visitedTimes[neighbor])