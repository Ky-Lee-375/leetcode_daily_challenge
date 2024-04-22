class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # construct a graph or a tree
        graph = collections.defaultdict(set)
        for node, parent in enumerate(parents):
            graph[parent].add(node)
        n = len(parents)
        
        d = collections.Counter()
        # using DFS
        def dfs(node):
            p, sum_ = 1, 0
        # remove each node
            for child in graph[node]:
                res = dfs(child)
                p *= res
                sum_ += res
            p *= max(1, n-1-sum_)
            d[p] += 1
            return sum_+1
            # compute the product of size of connected compotent?
            # save it in dictionary += 1
        # return highest val in dict
        dfs(0)
        return d[max(d.keys())]