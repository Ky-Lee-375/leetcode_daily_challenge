class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:        
        root = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)
        
        def find(x):
            if x == root[x]:
                return x
            
            root[x] = find(root[x])
            return root[x]
        
        
        def union(n1, n2):
            r1 = find(n1)
            r2 = find(n2)
            
            if r1 == r2:
                return False
            
            if r1 != r2:
                if rank[r1] > rank[r2]:
                    root[r2] = r1
                    rank[r1] += 1
                else:
                    root[r1] = r2
                    rank[r2] += 1
            
            return True
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]
            