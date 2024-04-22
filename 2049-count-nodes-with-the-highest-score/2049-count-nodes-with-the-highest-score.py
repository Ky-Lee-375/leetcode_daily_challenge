class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:            
        # construct a graph
        graph = collections.defaultdict(set)
        for node, parent in enumerate(parents):
            graph[parent].add(node)
        # dictionary for a counter
        d = collections.Counter()
        n = len(parents)
        # DFS: Iterate over a graph
        def dfs(node):
        # delete one node at a time
            product, total = 1, 0
            # count children of each node
            for child in graph[node]:
                res = dfs(child)
                product *= res
                total += res
            product *= max(1, n -1 - total)
            d[product] += 1
            
            return total +1
            # count connected component
            # increment in dictionary
            # return num elemen in the CC
        
        # Call DFS
        dfs(0)
        # return max of the counter
        return d[max(d.keys())]