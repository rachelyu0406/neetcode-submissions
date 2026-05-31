# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)

        res = []

        while q:
            temp = []
            for i in range(len(q)):
                if q[0]:
                    q.append(q[0].left)
                    q.append(q[0].right)
                    temp.append(q[0].val)
                q.popleft()
            if temp:
                res.append(temp)
        return res
        