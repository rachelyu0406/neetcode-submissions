class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     hashMap = {}
    #     index = []
    #     for i in range(len(nums)):
    #         if target - nums[i] in hashMap:
    #             index.append(hashMap.get(target - nums[i]))
    #             index.append(i)
    #         else:
    #             hashMap[nums[i]] = i
    #     return index

        hashMap = {}
        for i in range(len(nums)):
            hashMap[target - nums[i]] = i

        res = []

        for i in range(len(nums)):
            if nums[i] in hashMap and hashMap[nums[i]] != i:
                res.append(i)
                res.append(hashMap[nums[i]])
                break
        
        return res



        