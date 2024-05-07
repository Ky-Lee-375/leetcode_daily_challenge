class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # compose an undirected graph
        G = collections.defaultdict(list)
        for u,v,w in edges:
            G[u].append((v,w))
            G[v].append((u,w))
        
        # dfs(node, visited, gain, cost)
        # recursively call dfs on neighbor
        def dfs(node, visited, gain, cost):
            if node == 0:
                self.ans = max(self.ans, gain)
            for neighbor, w in G[node]:
                if w <= cost:
                    dfs(neighbor, visited | set([neighbor]), gain + (neighbor not in visited)*values[neighbor], cost-w)
        
        # self.ans = 0
        # call dfs
        # return self.ans
        self.ans = 0
        dfs(0, set([0]), values[0], maxTime)
        return self.ans
        
        