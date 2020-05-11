# Review the following link for the question prompt: https://leetcode.com/problems/symmetric-tree/

# O(N) time | O(d) space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return (root is None) or (self.isSymmetricHelper(root.left, root.right))
    
    def isSymmetricHelper(self, left: TreeNode, right: TreeNode) -> bool:
        
        if left is None or right is None:
            return left == right
        
        return (left.val == right.val) \
                and self.isSymmetricHelper(left.left, right.right) \
                and self.isSymmetricHelper(left.right, right.left)