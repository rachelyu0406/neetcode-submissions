# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# go left/ right if both are greater/ smaller. 
# else just return since its the lowest
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        if curr.val > p.val and curr.val > q.val:
            return self.lowestCommonAncestor(curr.left, p, q)
        elif curr.val < p.val and curr.val < q.val:
            return self.lowestCommonAncestor(curr.right, p, q)
        else:
            return curr
        