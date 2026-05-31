class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            roota = find(a)
            rootb = find(b)

            if roota == rootb:
                return False
            
            parent[roota] = rootb
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]