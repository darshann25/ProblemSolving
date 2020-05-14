# Review the following link for the question prompt: https://leetcode.com/problems/copy-list-with-random-pointer/

# O(N) time | O(N) space
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head: return None
        
        newHead = Node(head.val, None, None)
        runningNode = newHead
        node = head
        
        nodeMemory = {head: newHead}
        node = node.next
        
        while node:
            newNode = Node(node.val, None, None)
            runningNode.next = newNode
            runningNode = runningNode.next
            
            nodeMemory[node] = runningNode
            node = node.next
            
        runningNode = newHead
        while runningNode:
            if head.random:
                runningNode.random = nodeMemory[head.random]
                    
            runningNode = runningNode.next
            head = head.next
            
        return newHead