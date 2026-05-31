# Sliding window with a frequency map.
# Expand r to add characters into the window.
# If s[r] becomes a duplicate, move l right until the duplicate is removed.
# Track the largest valid window with no repeated characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        maxLength = 0
        freq = {}
        l, r = 0, 1
        freq[s[0]] = 1
        while r < len(s):
            if s[r] not in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1
            if freq[s[r]] > 1:
                while freq[s[r]] > 1:
                    freq[s[l]] -= 1
                    l += 1
            maxLength = max(maxLength, r - l + 1)
            r += 1
        return maxLength