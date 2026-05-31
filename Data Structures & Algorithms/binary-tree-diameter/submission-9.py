# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = -1
        def dfs(root):
            nonlocal maxDiam
            if not root:
                return -1
            leftLen = dfs(root.left)
            rightLen = dfs(root.right)
            maxDepth = 1 + max(leftLen, rightLen)
            maxDiam = max(leftLen + rightLen + 2, maxDepth, maxDiam)
            print(root, maxDiam)
            return maxDepth
        dfs(root)
        return maxDiam
        