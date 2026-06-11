class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7
        n = len(edges) + 1

        if n == 1:
            return 0

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            depth = 0

            for nei in graph[node]:
                if nei != parent:
                    depth = max(depth, 1 + dfs(nei, node))

            return depth

        max_depth = dfs(1, 0)

        return pow(2, max_depth - 1, MOD)
        