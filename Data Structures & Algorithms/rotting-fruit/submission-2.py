class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        numFresh = 0
        count = 0

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    numFresh += 1
        # can also do it like this
        """
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                ...

            time == 1
            """
        while q:
            curr = []
            while q:
                r, c = q.popleft()
                curr.append((r, c))
            print(curr)
            print(minutes)

            for r, c in curr:
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < rows and 0 <= nc < cols 
                    and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        count += 1
            if not q:
                continue
                        
            minutes += 1
        return minutes if count == numFresh else -1
        