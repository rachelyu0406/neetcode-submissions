# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                print(True, 0)
                return (True, 0)
            Lflag, Llength = dfs(root.left)
            Rflag, Rlength = dfs(root.right)
            if not Lflag or not Rflag or abs(Llength - Rlength) > 1:
                print(root, False, Llength + 1)
                return (False, Llength + 1)
            else:
                print(root, True, max(Llength, Rlength) + 1)
                return (True, max(Llength, Rlength) + 1)
        a, b = dfs(root)
        return a
        