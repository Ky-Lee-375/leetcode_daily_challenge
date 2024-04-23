class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # visited list
        visited = [[-1]*COLS for _ in range(ROWS)]
        # direction
        direction = [(0,1), (0,-1), (1,0), (-1,0)]
        # dfs
        def dfs(r, c):
            if visited[r][c] != -1:
                return visited[r][c]
            counter = 1
            
            for d in direction:
                res = 1
                next_r, next_c = r + d[0], c + d[1]
                if 0<= next_r < ROWS and 0 <= next_c < COLS:
                    if matrix[r][c] < matrix[next_r][next_c]:
                        res = 1 + dfs(next_r, next_c)
                counter = max(counter, res)
            visited[r][c] = counter
            return counter
        
        max_path = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_path = max(max_path, dfs(r,c))
        return max_path
                
    
# 1. Print the longest path
# 2. Print all the paths that are strictly increasing.
# 3. Print all non-decreasing path
                    
        
        
        