class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, 0
        q = deque()

        while r < len(nums):
            # remove the smaller values before adding in the max
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left most value (by index) if window shifts
            if l > q[0]:
                q.popleft()
            
            # check if window is size k then append max value & l increase
            # right always increases no matter what since at beginning we only increase right
            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res