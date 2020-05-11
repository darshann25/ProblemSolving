# Review the following link for the question prompt: https://leetcode.com/problems/validate-binary-search-tree/

# O(N) time | O(d) space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBSTHelper(self, tree: TreeNode, minVal: float, maxVal: float) -> bool:
        if tree is None:
            return True
        if tree.val <= minVal or tree.val >= maxVal:
            return False

        leftIsValid = self.isValidBSTHelper(tree.left, minVal, tree.val)
        rightIsValid = self.isValidBSTHelper(tree.right, tree.val, maxVal)

        return leftIsValid and rightIsValid
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTHelper(root, float('-inf'), float('inf'))