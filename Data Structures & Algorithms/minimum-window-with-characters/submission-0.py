class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        l = 0
        have, need = {}, {}
        res, resLen = [-1, -1], float('inf')
        for c in t:
            need[c] = 1 + need.get(c, 0)
        h, n = 0, len(need)
        for r in range(len(s)):
            c = s[r]
            have[c] = 1 + have.get(c, 0)
            if c in need and have[c] == need[c]:
                h += 1
            while h == n:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    h -= 1
                l += 1
        if resLen != float('inf'):
            return s[res[0]: res[1] + 1]
        else:
            return ''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''l = 0
        res = ''
        freq = {}
        count = len(t)
        for c in t:
            freq[c] = 1 + freq.get(c, 0)
        while s[l] not in freq and l < len(s):
            l += 1
        occurences = []
        for r in range(l, len(s)):
            if freq.get(s[r], 0) != 0:
                freq[s[r]] -= 1
                occurences.append(r)
                count -= 1
                if count == 0:
                    if res == '':
                        res = s[l:r + 1]
                    if r - l + 1 < len(res):
                        res = s[l:r + 1]
                    freq[s[occurences[0]]] += 1
                    l = occurences[0] + 1
                    occurences.pop(0)
                    count += 1
        return res'''