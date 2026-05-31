class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        numComponents = n

        for u, v in edges:
            rootu = find(u)
            rootv = find(v)

            if rootu != rootv:
                # importanttt i got this wrong before don't use parents[u] = parents[v]
                parents[rootu] = rootv
                numComponents -= 1
            else:
                continue
        
        return numComponents
        