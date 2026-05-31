class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

        # my solution
        """n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        best = [float("-inf")] * n
        best[n - 1] = nums[n - 1]
        best[n - 2] = nums[n - 2]
        best[n - 3] = nums[n - 1] + nums [n - 3]
        for i in range(n - 4, -1, -1):
            best[i] = nums[i] + max(best[i + 2], best[i + 3])
        print(best)
        return max(best[0], best[1])"""
        