# Review the following link for the question prompt: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# O(N) time | O(d) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.getLowestCommonAncestor(root, p, q).lowestCommonAncestor
    
    def getLowestCommonAncestor(self, node, p, q):
        
        if node is None: return Node(None, 0)
        
        numImportantDescendants = 0
        nodeLeft = self.getLowestCommonAncestor(node.left, p, q)
        if nodeLeft.lowestCommonAncestor is not None:
            return nodeLeft
        
        nodeRight = self.getLowestCommonAncestor(node.right, p, q)
        if nodeRight.lowestCommonAncestor is not None:
            return nodeRight
        numImportantDescendants += nodeLeft.numImportantDescendants + nodeRight.numImportantDescendants
        
        if node == p or node == q:
            numImportantDescendants += 1
        lowestCommonAncestor = node if numImportantDescendants == 2 else None
        return Node(lowestCommonAncestor, numImportantDescendants)
            
            
class Node:
    def __init__(self, lowestCommonAncestor, numImportantDescendants):
        self.lowestCommonAncestor = lowestCommonAncestor
        self.numImportantDescendants = numImportantDescendants