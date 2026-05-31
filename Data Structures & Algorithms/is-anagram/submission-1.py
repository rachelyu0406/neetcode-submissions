class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters1 = {}
        letters2 = {}
        for l in s:
            if l in letters1:
                letters1[l] = letters1[l] + 1
            else:
                letters1[l] = 1
        for j in t:
            if j in letters2:
                letters2[j] = letters2[j] + 1
            else:
                letters2[j] = 1
        return letters1 == letters2
        