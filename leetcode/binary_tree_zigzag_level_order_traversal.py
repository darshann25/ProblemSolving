# Review the following link for the question prompt: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# O(N + N/2) time | O(N + d) space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        bfsArray = []
        bfsArray = self.levelOrderHelper(root, 0, bfsArray)
        
        for depth in range(len(bfsArray)):
            if depth % 2 == 1:
                depthArray = bfsArray[depth]
                bfsArray[depth] = depthArray[::-1]
        
        return bfsArray
    
    def levelOrderHelper(self, node: TreeNode, depth: int, bfsArray: List[List[int]]) -> List[List[int]]:

        if node is None:
            return bfsArray
        
        if depth < len(bfsArray):
            depthArray = bfsArray[depth]
            depthArray.append(node.val)
            bfsArray[depth] = depthArray
        else:
            bfsArray.append([node.val])
        
        bfsArray = self.levelOrderHelper(node.left, depth+1, bfsArray)
        bfsArray = self.levelOrderHelper(node.right, depth+1, bfsArray)
        return bfsArray