class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if a + nums[l] + nums[r] == 0:
                    res.append([a, nums[l], nums[r]])
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    while r > l and nums[r - 1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                elif a + nums[l] + nums[r] <= 0:
                    l += 1
                else:
                    r -= 1
        return res