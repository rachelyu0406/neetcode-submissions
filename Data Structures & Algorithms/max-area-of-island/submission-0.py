class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            area = 0
            while q:
                row, col = q.popleft()
                area += 1
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if ((r, c) not in visited 
                    and r in range(rows) and c in range(cols) 
                    and grid[r][c] == 1):
                        q.append((r, c))
                        visited.add((r, c))
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    maxArea = max(area, maxArea)
        return maxArea