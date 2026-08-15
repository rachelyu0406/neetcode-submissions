# [4,5,6,7,0,1,2]
#  0 1 2 3 4 5 6
#  l       l   r
#  m = 3

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (r + l) // 2
            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        if nums[l] == target:
            return l
        return -1
        