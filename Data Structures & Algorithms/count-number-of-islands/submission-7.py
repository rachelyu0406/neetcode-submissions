class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        res = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                    dfs(nr, nc)
            return
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    if grid[r][c] == "0":
                        visited.add((r, c))
                        continue
                    else:
                        dfs(r, c)
                        res += 1
        return res
        