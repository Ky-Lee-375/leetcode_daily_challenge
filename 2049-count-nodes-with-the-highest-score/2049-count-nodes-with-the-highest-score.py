class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # create a graph first
        graph = collections.defaultdict(set)
        for node, parent in enumerate(parents):
            graph[parent].add(node)
        
        d = collections.Counter()
        # dfs
        # find the leaf node
        # sum counter, product 
        def dfs(node):
            product, counter = 1,0
            for child in graph[node]:
                res = dfs(child)
                product *= res
                counter += res
            # compute the score
            product *= max(1, len(parents)-counter-1)
            d[product] += 1
            return counter +1
        
        dfs(0)
        return d[max(d.keys())]
        
        # result counter dict