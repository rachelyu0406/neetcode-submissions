class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letterMap = {2: "abc", 3: "def", 4: "ghi", 5: "jkl",
        6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        def dfs(curCombination, i):
            if i >= len(digits):
                if curCombination:
                    res.append("".join(curCombination))
                return
            for j in letterMap[int(digits[i])]:
                curCombination.append(j)
                dfs(curCombination, i + 1)
                curCombination.pop()
        dfs([], 0)
        return res