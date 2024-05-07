class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        G = defaultdict(list)
        for u, v, c in edges:
            G[u].append((v, c))
            G[v].append((u, c))
            
        def dfs(node, visited, gain, cost):
            if node == 0: 
                self.ans = max(self.ans, gain)
            for neib, w in G[node]:
                if w <= cost:
                    dfs(neib, visited | set([neib]), gain + (neib not in visited) * values[neib], cost - w)

        self.ans = 0
        dfs(0, set([0]), values[0], maxTime)
        return self.ans
        