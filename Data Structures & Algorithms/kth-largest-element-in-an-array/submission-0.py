class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for n in nums:
            heapq.heappush(maxHeap, -1 * n)
        i = k
        res = 0
        while i > 0:
            res = -1 * heapq.heappop(maxHeap)
            i -= 1
        return res
        