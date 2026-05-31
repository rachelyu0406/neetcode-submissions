class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        visited = set()
        for i in range(rows):
            if board[i][0] == "O":
                q.append((i, 0))
                visited.add((i, 0))
            print(i, cols - 1)
            if board[i][cols - 1] == "O":
                q.append((i, cols - 1))
                visited.add((i, cols - 1))
        for i in range(cols):
            if board[0][i] == "O":
                q.append((0, i))
                visited.add((0, i))
            if board[rows - 1][i] == "O":
                q.append((rows - 1, i))
                visited.add((rows - 1, i))
        print(visited)

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if (0 <= nr < rows
                and 0 <= nc < cols
                and (nr, nc) not in visited
                and board[nr][nc] == "O"):
                    visited.add((nr, nc))
                    q.append((nr, nc))
        print(visited)
        for i in range(rows):
            for j in range(cols):
                print(i, j)
                if not({(i, j)} & visited):
                    board[i][j] = "X"
        