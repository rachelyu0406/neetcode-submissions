class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # dfs solution
        if n == 0:
            return True

        adj = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n

        # union find solution
        """
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in edges:
            root_u, root_v = find(u), find(v)
            if root_u == root_v: return False # cycle detected
            parent[root_u] = root_v
        
        return True
        """
        