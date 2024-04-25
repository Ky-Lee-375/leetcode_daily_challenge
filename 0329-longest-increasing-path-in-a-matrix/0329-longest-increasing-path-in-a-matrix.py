class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # edge case : not matrix
        if not matrix:
            return 0
        
        # declare variables
        # ROWS, COLS
        # visit array
        # direction
        ROWS, COLS, = len(matrix), len(matrix[0])
        visit = [[-1]*COLS for _ in range(ROWS)]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        # def dfs(r,c)
        # base case: if seen in visit
        # return the val
        def dfs(r,c):
            if visit[r][c] != -1:
                return visit[r][c]
            
            # if not, from (r,c)
            # move all directions
            # check if anything is strictly greater
            # return the max length
            counter = 1
            for d in directions:
                tmp = 1
                next_r, next_c = r +d[0], c + d[1]
                if 0<= next_r< ROWS and 0<= next_c < COLS and matrix[r][c] < matrix[next_r][next_c]:
                    tmp =  1+ dfs(next_r, next_c)
                counter = max(counter, tmp)
            visit[r][c] = counter
            return counter
        
        # call dfs on every loc
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r,c))
        # return the max
        return res
    
# 1. Print the longest path
# 2. Print all the paths that are strictly increasing.
# 3. Print all non-decreasing path
                    
        
        
        