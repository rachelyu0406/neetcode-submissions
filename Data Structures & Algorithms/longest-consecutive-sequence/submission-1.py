class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use a set for O(1) lookup.
        # Only count from the start of a sequence: n - 1 not in set.
        # Expand upward and track the longest streak.
        length = 0
        maxLength = 0
        start = 0
        numSet = set(nums)
        for n in nums:
            if n - 1 not in numSet:
                start = n
                while start in numSet:
                    length += 1
                    start += 1
                maxLength = max(maxLength, length)
                length = 0
        return maxLength
        