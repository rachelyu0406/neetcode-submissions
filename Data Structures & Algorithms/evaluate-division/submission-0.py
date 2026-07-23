class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            value = values[i]

            graph[a].append((b, value))
            graph[b].append((a, 1/value))
        
        def dfs(curProduct, curNum, end, visited):
            if curNum == end:
                return curProduct
            visited.add(curNum)
            for nei, weight in graph[curNum]:
                if nei not in visited:
                    curAns = dfs(curProduct * weight, nei, end, visited)
                    if curAns != -1.0:
                        return curAns
            return -1.0
        
        res = []
        for query in queries:
            start = query[0]
            end = query[1]
            if start not in graph or end not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(1.0, start, end, set()))
        return res