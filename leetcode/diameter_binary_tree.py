# Review the following link for the question prompt: https://leetcode.com/problems/diameter-of-binary-tree/

# 0(d) time | O(1) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        leftHeight = self.heightOfBinaryTree(root.left)
        rightHeight = self.heightOfBinaryTree(root.right)
        
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)
        
        return max(leftHeight + rightHeight, leftDiameter, rightDiameter)

    def heightOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.heightOfBinaryTree(root.left),self.heightOfBinaryTree(root.right))