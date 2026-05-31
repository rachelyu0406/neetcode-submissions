class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pSet = set()
        aSet = set()
        # visited = set()
        pdirections = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        adirections = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        d = deque()
        rows = len(heights)
        cols = len(heights[0])
        # pSet.add((0,0))
        # aSet.add((rows - 1, cols - 1))
        for i in range(0, rows):
            q.append((i, 0))
            pSet.add((i, 0))
        for j in range(0, cols):
            q.append((0, j))
            pSet.add((0, j))
        for i in range(rows - 1, -1, -1):
            d.append((i, cols - 1))
            aSet.add((i, cols - 1))
        for j in range(cols - 1, -1, -1):
            d.append((rows - 1, j))
            aSet.add((rows - 1, j))
        print("curr pSet: ", pSet)
        print("curr aSet: ", aSet)
        while q:
            r, c = q.popleft()
            # visited.add((r, c))
            # if r == 1 and c == 3:
                # print("popped: ", r, c)
            for dr, dc in pdirections:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < rows
                and 0 <= nc < cols
                # and (nr, nc) not in visited
                and (nr, nc) not in pSet
                and heights[nr][nc] >= heights[r][c]):
                    q.append((nr, nc))
                    pSet.add((nr, nc))
                    # if r == 1 and c == 3:
                        # print("added: ", nr, nc)
        while d:
            r, c = d.popleft()
            # visited.add((r, c))
            for dr, dc in adirections:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < rows
                and 0 <= nc < cols
                # and (nr, nc) not in visited
                and (nr, nc) not in aSet 
                and heights[nr][nc] >= heights[r][c]):
                    d.append((nr, nc))
                    aSet.add((nr, nc))

        print(pSet)
        print(aSet)
        res = []
        for a, b in pSet:
            if (a, b) in aSet:
                res.append([a, b])
        res.sort()
        return res








        # old solution not finished
        """pSet = set()
        aSet = set()
        def dfsp(node):
            

        for i in range(len(heights)):
            dfsp(heights[i][0])
            dfsa(heights[i][len(heights[0]) - 1])
        for i in range(1, len(heights[0])):
            dfsp(heights[0][i])
            dfsa(heights[len(heights) - 1][i])

        """