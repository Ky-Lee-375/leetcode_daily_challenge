class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # edge case
        if not matrix:
            return 0
        # variable declaration
        # row, col, direction
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]        
        
        # dfs + memoization
        visit = [[-1]*COLS for _ in range(ROWS)]
        # from current loc, move direction
        # if strictly greater, than recursively call dfs
        # +1 
        def dfs(r,c):
            if visit[r][c] != -1:
                return visit[r][c]
            res = 1
            for d in directions:
                next_row, next_col = r +d[0], c + d[1]
                if (0<= next_row<ROWS) and (0 <= next_col <COLS) and matrix[r][c] < matrix[next_row][next_col]:
                    res = max(res, 1+ dfs(next_row, next_col))
                visit[r][c] = res
            return res
        final = 0
        for r in range(ROWS):
            for c in range(COLS):
                final = max(final, dfs(r,c))
        return final
        
        
# 1. Print the longest path
# 2. Print all the paths that are strictly increasing.
# 3. Print all non-decreasing path
                    
        
        
        