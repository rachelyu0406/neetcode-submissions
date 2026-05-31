class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def checklmr(l, m ,r):
            if target == nums[l]:
                return l
            if target == nums[m]:
                return m
            if target == nums[r]:
                return r
            
        res = 0
        l , r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            res = checklmr(l, m, r)
            if res is not None:
                return res
            if nums[l] < nums[r]:
                if target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] >= nums[l]:
                    if target > nums[m]:
                        l = m + 1
                    else:
                        if target > nums[l]:
                            r = m - 1
                        else:
                            l = m + 1
                else:
                    if target < nums[m]:
                        r = m - 1
                    else:
                        if target < nums[r]:
                            l = m + 1
                        else:
                            r = m - 1
        return -1
                

    