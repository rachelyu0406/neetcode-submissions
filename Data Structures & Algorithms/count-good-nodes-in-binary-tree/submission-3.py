# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS through the tree while carrying the max value seen on the path from root.
# A node is good if its value is >= the max value seen before it.
# After checking the current node, update maxVal and pass it to both children.
# Return the number of good nodes from left subtree + right subtree + current node if good.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0
            if maxVal <= root.val:
                maxVal = max(root.val, maxVal)
                return 1 + dfs(root.left, maxVal) + dfs(root.right, maxVal)
            else:
                maxVal = max(root.val, maxVal)
                return dfs(root.left, maxVal) + dfs(root.right, maxVal)
        return dfs(root, float("-inf"))
        