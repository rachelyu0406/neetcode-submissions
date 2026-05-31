class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        visited = set()
        maxTime  = 0
        
        for u, v, w in times:
            adj[u].append((v, w))
        
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            print(time, node)
            if node in visited:
                continue
            maxTime = max(maxTime, time)
            visited.add(node)
            print(maxTime)
            for nei, weight in adj[node]:
                heapq.heappush(heap, (time + weight, nei))
                print("added: ", time + weight, nei)
        return maxTime if len(visited) == n else -1