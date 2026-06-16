# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS through the tree while keeping a valid range for each node.
# For a BST, every node must be strictly greater than its left bound
# and strictly less than its right bound.
# Left child range becomes (left, node.val).
# Right child range becomes (node.val, right).
# If any node breaks its allowed range, return False.

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float("-infinity"), float("infinity"))