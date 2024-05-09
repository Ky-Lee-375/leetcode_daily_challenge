class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # construct a graph
        graph = collections.defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))

        
        # add curr val
        def dfs(node, visited, gain, time):
            if node == 0:
                self.ans = max(self.ans, gain)
            for neighbor, w in graph[node]:
                if w <= time:
                    dfs(neighbor, visited|set([neighbor]), gain + (neighbor not in visited)*values[neighbor], time-w)
        
        self.ans = 0
        dfs(0, set([0]), values[0], maxTime)
        return self.ans