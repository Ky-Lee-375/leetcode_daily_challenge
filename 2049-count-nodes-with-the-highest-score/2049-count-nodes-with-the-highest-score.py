class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # construct a graph
        graph = collections.defaultdict(list)
        for node, parent in enumerate(parents):
            graph[parent].append(node)
        d = collections.Counter()
        n = len(parents)
        # dfs
        # find the score from the leaf
        def dfs(node):
            total, product = 0, 1
            for child in graph[node]:
                res = dfs(child)
                total += res
                product *= res
            
            product *= max(1, n-total-1)
            d[product] += 1
            return total +1
        
        dfs(0)
        return d[max(d.keys())]