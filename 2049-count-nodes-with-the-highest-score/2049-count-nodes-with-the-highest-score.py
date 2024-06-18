class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # compute the score
        # return # of nodes w highest score
        
        # create a graph from a list
        # using enumerate
        graph = collections.defaultdict(list)
        for idx, parent in enumerate(parents):
            graph[parent].append(idx)

        d = collections.Counter()
        n = len(parents)
        
        # Using dfs
        # size of two subtree
        # multiply size of two subtrees
        def dfs(node):
            total, product = 0,1
            for child in graph[node]:
                res = dfs(child)
                total += res
                product *= res
            
            product *= max(1, n-total-1)
            d[product] += 1
            return total +1
        dfs(0)
        return d[max(d.keys())]
            
        
        
        