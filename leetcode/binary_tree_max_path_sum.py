# Review the following link for the question prompt: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# O(N) time | O(log(N)) space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        _, maxPathSum = self.findMaxSum(root)
        return maxPathSum
    
    def findMaxSum(self, node: TreeNode):
        if node is None:
            return (0,float('-inf'))
        
        leftMaxSumAsBranch, leftMaxSum = self.findMaxSum(node.left)
        rightMaxSumAsBranch, rightMaxSum = self.findMaxSum(node.right)

        maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
        maxSumAsBranch = max(maxChildSumAsBranch + node.val, node.val)
        maxSumAsRootNode = max(leftMaxSumAsBranch + node.val + rightMaxSumAsBranch, maxSumAsBranch)
        maxPathSum = max(leftMaxSum, rightMaxSum, maxSumAsRootNode)

        return maxSumAsBranch, maxPathSum