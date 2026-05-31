        # Hierholzer’s algorithm for an Eulerian path
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u, v in tickets:
            heapq.heappush(adj[u], v)
        res = []

        def dfs(curr):
            while adj[curr]:
                nextCity = heapq.heappop(adj[curr])
                dfs(nextCity)
            res.append(curr)
        
        dfs("JFK")
        
        # reverse res
        return res[::-1]





# does not work
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        count = defaultdict(int)
        for u, v in tickets:
            count[u] += 1
            count[v] += 1
        singles = set()
        end = ""
        potentials = set()
        for a in count:
            if count[a] == 1:
                end = a
            if count[a] == 2:
                potentials.add(a)
        print("singles", singles)
        adj = defaultdict(list)
        for u, v in tickets:
            heapq.heappush(adj[u], v)
        visited = set()
        curr = "JFK"
        res = []
        
        while not(len(visited) == len(adj) and (len(tickets) + 1) == len(res)):
            visited.add(curr)
            res.append(curr)
            print(curr)
            print("adj", adj)
            print("res", res)
            print(len(res), len(tickets))
            if (len(res) == len(tickets) + 1):
                break
            nextCity = heapq.heappop(adj[curr])
            if len(adj[curr]) > 1 and nextCity in singles:
                    temp = nextCity
                    nextCity = heapq.heappop(adj[curr])
                    heapq.heappush(temp)
            curr = nextCity
        return res
"""