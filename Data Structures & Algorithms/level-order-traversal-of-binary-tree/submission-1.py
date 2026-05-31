# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# q[0] is the front node in the queue.
# If it exists, add its left and right children to the queue and save its value.
# Then pop it from the queue.
# len(q) freezes the current level size, so newly added children are processed next level.

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
        