class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        index = []
        for i in range(len(nums)):
            if (target - nums[i] in hashMap):
                index.append(hashMap.get(target - nums[i]))
                index.append(i)
            else:
                hashMap[nums[i]] = i
        return index


        