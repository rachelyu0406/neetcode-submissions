class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1] * (len(nums) + 1)
        s = [1] * (len(nums) + 1)
        res = [0] * len(nums)
        for i in range(len(nums)):
            p[i + 1] = p[i] * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            s[i - 1] = s[i] * nums[i]
        for i in range(len(nums)):
            res[i] = p[i] * s[i]

        return res