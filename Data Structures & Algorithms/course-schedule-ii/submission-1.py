class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for p in prerequisites:
            adj[p[1]].append(p[0])
            indegree[p[0]] += 1

        ordering = [] 

        queue = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            ordering.append(course)

            for nextCourse in adj[course]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)
        return ordering if len(ordering) == numCourses else []
                