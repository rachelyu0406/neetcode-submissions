# Bucket Sort:
# 1. Count the frequency of each number.
# 2. Use an array where index = frequency (bucket[3] holds numbers appearing 3 times).
# 3. Fill the buckets.
# 4. Traverse buckets from highest frequency to lowest until k elements are collected.
#
# Time: O(n)
# Space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = defaultdict(int)
        array = [[] for _ in range(len(nums) + 1)]
        res = []

        for n in nums:
            if n in hMap:
                hMap[n] += 1
            else:
                hMap[n] = 1
        
        for num, freq in hMap.items():
            array[freq].append(num)
        
        i = 0
        n = 0
        while n < k:
            for j in range(len(array[len(array)- 1 - i])):
                res.append(array[len(array)- 1 - i][j])
                n += 1
            i += 1
        
        return res
        

        