# min spanning tree: Prim’s Algorithm
# Best when you have an adjacency list.
# Start from any node.
# Repeatedly add the cheapest edge that 
# connects visited nodes to unvisited nodes.
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for xi, yi in points:
            for xj, yj in points:
                distance = abs(xi - xj) + abs(yi - yj)
                adj[(xi, yi)].append((distance, xj, yj))
                adj[(xj, yj)].append((distance, xi, yi))
        minheap = [(0, points[0][0], points[0][1])]
        total = 0
        visited = set()
        while len(visited) < len(points) and minheap:
            w, xi, yi = heapq.heappop(minheap)
            if (xi, yi) in visited:
                continue
            visited.add((xi, yi))
            total += w
            for distance, xj, yj in adj[(xi, yi)]:
                if (xj, yj) not in visited:
                    heapq.heappush(minheap, (distance, xj, yj))
        return total

        