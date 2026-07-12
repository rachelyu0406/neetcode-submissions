class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        # two types of sliding windo. fixed len and variable len
        # this is fixed len
        target = defaultdict(int)

        # Count characters in s1
        for c in s1:
            target[c] += 1

        cur = defaultdict(int)

        l = 0

        for r in range(len(s2)):
            # Add current character to window
            cur[s2[r]] += 1

            # Keep window size equal to len(s1)
            if r - l + 1 > len(s1):
                cur[s2[l]] -= 1
                if cur[s2[l]] == 0:
                    del cur[s2[l]]
                l += 1

            # Check if window is a permutation
            if cur == target:
                return True

        return False
        """
        target = defaultdict(int)
        for l in s1:
            target[l] += 1
        l, r = 0, len(s2) - 1
        flag = True
        cur = defaultdict(int)
        while l < r:
            print(l, r)
            temp = False
            if s2[l] not in target:
                if s2[l] in cur:
                    cur[s2[l]] -= 1
                    if cur[s2[l]] == 0:
                        del cur[s2[l]]
                l += 1
                continue
            if s2[r] not in target:
                if s2[r] in cur:
                    cur[s2[r]] -= 1
                    if cur[s2[r]] == 0:
                        del cur[s2[r]]
                r -= 1
                continue
            if flag:
                for i in range(l, r + 1):
                    cur[s2[i]] += 1
                flag = False
            print(cur, target)
            if cur == target:
                return True
            else:
                if cur[s2[l]] > target[s2[l]]:
                    cur[s2[l]] -= 1
                    if cur[s2[l]] == 0:
                        del cur[s2[l]]
                    l += 1
                    temp = True
                if cur[s2[r]] > target[s2[r]]:
                    cur[s2[r]] -= 1
                    if cur[s2[r]] == 0:
                        del cur[s2[r]]
                    r -= 1
                    temp = True
                else:
                    if not temp:
                        print(1)
                        return False
        print(l, r)
        print(s2[l], s1)
        if l == r and len(s1) == 1 and s2[l] == s1:
            return True
        return False
        """