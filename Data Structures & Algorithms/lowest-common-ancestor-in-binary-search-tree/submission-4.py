# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# go left/ right if both are greater/ smaller. 
# else just return since its the lowest

# Since this is a BST:
# If both p and q are smaller than curr, LCA must be in the left subtree.
# If both p and q are larger than curr, LCA must be in the right subtree.
# Otherwise, curr is the split point, so curr is the lowest common ancestor.
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        if curr.val > p.val and curr.val > q.val:
            return self.lowestCommonAncestor(curr.left, p, q)
        elif curr.val < p.val and curr.val < q.val:
            return self.lowestCommonAncestor(curr.right, p, q)
        else:
            return curr
        