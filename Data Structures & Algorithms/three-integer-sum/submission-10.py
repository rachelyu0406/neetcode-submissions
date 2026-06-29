
# Sort nums, then fix one number and use two pointers after that num to find pairs
# that sum to its opposite. Skip duplicates for i, l, (r is guranteed to be unique)
# repeated triplets. Time: O(n^2), extra space: O(1).

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                # optional but make it faster (early stopping)
                break
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                curL = nums[l]
                curR = nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == curL:
                        l += 1
                    while l < r and nums[r] == curR:
                        r -= 1
                elif total < 0:
                    l += 1
                    while l < r and nums[l] == curL:
                        l += 1
                else:
                    r -= 1
                    # while l < r and nums[r] == curR:
                    #     r -= 1
                
        return res
        