# use backtracking and for each r, c run dfs four ways

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if not(0 <= r < rows and 0 <= c < cols 
            and word[i] == board[r][c] and (r, c) not in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
        