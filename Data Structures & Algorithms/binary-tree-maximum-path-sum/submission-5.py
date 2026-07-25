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
                return (float("-inf"), float("-inf"), float("-inf"))
            maxPathL, singlePathL, discontinueL = dfs(root.left)
            maxPathR, singlePathR, discontinueR = dfs(root.right)
            maxPathCur = root.val + singlePathL + singlePathR
            singlePathCur = max(root.val, root.val + singlePathL, 
            root.val + singlePathR)
            discontinue = max(discontinueL, discontinueR, singlePathCur)
            return(max(maxPathL, maxPathR, maxPathCur), singlePathCur, discontinue)
        
        maxPath, singlePath, discontinue = dfs(root)
        return max(maxPath, singlePath, discontinue)