class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    q = deque()
                    q.append((i, j))
                    visited.add((i, j))
                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc
                            if (0 <= nr < rows and 0 <= nc < cols and
                            grid[nr][nc] == "1" and (nr, nc) not in visited):
                                q.append((nr, nc))
                                visited.add((nr, nc))
                    count += 1
        return count

        