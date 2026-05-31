# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], i: Optional[TreeNode]) -> bool:
        if not i:
            return True
        if not root:
            return False
        if self.isSameTree(root, i):
            return True
        return(self.isSubtree(root.left, i) or self.isSubtree(root.right, i))
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return(self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        