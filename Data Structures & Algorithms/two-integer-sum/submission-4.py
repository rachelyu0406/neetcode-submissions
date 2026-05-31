class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}
        for i in range(len(nums)):
            difference[target - nums[i]] = i
        print(difference)
        
        for j in range(len(nums)):
            if nums[j] in difference and difference[nums[j]] != j:
                return [j, difference[nums[j]]]
        