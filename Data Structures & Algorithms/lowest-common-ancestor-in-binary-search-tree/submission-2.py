# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        if curr.val > p.val and curr.val > q.val:
            return self.lowestCommonAncestor(curr.left, p, q)
        elif curr.val < p.val and curr.val < q.val:
            return self.lowestCommonAncestor(curr.right, p, q)
        else:
            return curr
        