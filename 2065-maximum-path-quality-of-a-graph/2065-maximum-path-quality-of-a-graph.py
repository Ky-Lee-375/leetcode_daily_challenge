class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # construct a graph
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        
        self.ans = 0
        # dfs node, visit, gain, time
        # no return
        def dfs(node, visit, gain, time):
            if node == 0:
                self.ans = max(self.ans, gain) 
                
        # iterate child
            for child, w in graph[node]:
                if w <= time:
                    dfs(child, visit|set([child]), gain + (child not in visit)*values[child], time -w)
            
        # call dfs on the first elem
        dfs(0, set([0]), values[0], maxTime)
        return self.ans
    
# time: O(4^10)
# at most four edges are connected, num call: 100/10 = 10