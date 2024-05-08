class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dfs + memoization array
        # edge case
        # not matrix
        if not matrix:
            return 0
        
        # Declare variable
        # array, row, col
        # direction
        ROWS, COLS = len(matrix), len(matrix[0])
        visit = [[-1] * COLS for _ in range(ROWS)]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        # dfs (r,c)
        # check if it is in array
        def dfs(r,c):
            if visit[r][c] != -1:
                return visit[r][c]
        
        # move all direction
        # compare the value
            # counter variable
            # if greater, recursive call
            # increment the length
            # assign to array
            # return the counter
            res = 1
            for d in directions:
                # counter = 1
                next_r, next_c = r+d[0], c + d[1]
                if 0 <= next_r < ROWS and 0 <= next_c < COLS and matrix[r][c] < matrix[next_r][next_c]:
                    res = max(res, 1 + dfs(next_r, next_c))
                # res = max(res, counter)
            visit[r][c] = res
            return res
        
        # call dfs on every loc
        # get the max
        # return the max
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r,c))        
        return res
        
        
        
    
# 1. Print the longest path
# 2. Print all the paths that are strictly increasing.
# 3. Print all non-decreasing path
                    
        
        
        