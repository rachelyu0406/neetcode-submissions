class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        processed = 0
        while q:
            node = q.popleft()
            processed += 1

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if processed < numCourses:
            return False
        else:
            return True
        