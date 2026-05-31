class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] +=1
        for n in freq.values():
            if n > 1:
                return True
        return False
"""
         