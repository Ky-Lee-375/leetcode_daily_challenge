class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for e in prerequisites: adj[e[1]].append(e[0])
            
        result = [0] * numCourses
        
        def dfs(result, idx):
            if result[idx] == 1:
                return True
            if result[idx] == 2:
                return False
            result[idx] = 1
            
            for vert in adj[idx]:
                if dfs(result, vert):
                    return True
            result[idx] = 2
            return False
        for i in range(numCourses):
            if dfs(result, i):
                return False
        return True
        