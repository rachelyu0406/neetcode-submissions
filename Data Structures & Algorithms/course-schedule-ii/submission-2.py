class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        q = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        ordering = []
        processed = 0
        while q:
            node = q.popleft()
            ordering.append(node)
            processed += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if processed < numCourses:
            return []
        else:
            return ordering
        