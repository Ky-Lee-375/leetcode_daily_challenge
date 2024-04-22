class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # edge case
        if not matrix:
            return 0
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # direction: left, right, up, down
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        res = 0
        # DFS -> maintain a visited set
        visited = [[-1]*COLS for _ in range(ROWS)]
        def dfs(x, y):
            if visited[x][y] != -1:
                return visited[x][y]
                
            res = 1
            for d in directions:
                next_x = x + d[0]
                next_y = y + d[1]
                counter = 1
                if 0 <= next_x < ROWS and 0 <= next_y < COLS:
                    if matrix[x][y] < matrix[next_x][next_y]:
                        counter = 1 + dfs(next_x, next_y)
                res = max(res, counter)
            visited[x][y] = res
            return res
            
        for rows in range(ROWS):
            for cols in range(COLS):
                res = max(dfs(rows, cols), res)
        return res
                    
        
        
        