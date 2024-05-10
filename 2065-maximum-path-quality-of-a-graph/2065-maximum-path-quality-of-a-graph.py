class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # construct a graph
        graph = collections.defaultdict(list)
        for u,v,cost in edges:
            graph[u].append((v,cost))
            graph[v].append((u,cost))
            
        self.ans = 0
        # start from node 0
        # dfs node, visit, gain, time
        # keep track of max
        # return max
        def dfs(node, visit, gain, time):
            if node == 0:
                self.ans = max(self.ans, gain)
            for child, cost in graph[node]:
                if cost <= time:
                    dfs(child, visit|set([node]), gain + (child not in visit)*values[child], time-cost)
        
        # call dfs
        # return
        dfs(0, set([0]), values[0], maxTime)
        return self.ans