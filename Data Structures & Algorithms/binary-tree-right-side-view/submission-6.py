# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS by level.
# Process nodes left to right and store the last real node value in temp.
# The last value seen at each level is the right side view.
# Use temp is not None so node value 0 is not skipped.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []

        while q:
            print([n.val if n else None for n in q])
            temp = None
            for i in range(len(q)):
                if q[0]:
                    q.append(q[0].left)
                    q.append(q[0].right)
                    temp = q[0].val
                    print(temp)
                q.popleft()
            print(temp)
            if temp != None:
                res.append(temp)
        return res
        