# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (float("-inf"), float("-inf"))
            maxPathL, singlePathL = dfs(root.left)
            maxPathR, singlePathR = dfs(root.right)
            maxPathCur = root.val + singlePathL + singlePathR
            singlePathCur = max(root.val, root.val + singlePathL, 
            root.val + singlePathR)
            return(max(maxPathL, maxPathR, maxPathCur, singlePathCur), singlePathCur)
        
        maxPath, singlePath = dfs(root)
        return max(maxPath, singlePath)