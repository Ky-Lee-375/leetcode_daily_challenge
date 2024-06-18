class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # variable
        ROWS, COLS = len(grid1), len(grid1[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        # dfs that mark non subisland as 0
        def dfs(r, c, grid):
            grid[r][c] = 0
            
            for d in directions:
                next_r, next_c = r + d[0], c + d[1]
                if (0<=next_r<ROWS) and (0<=next_c<COLS) and grid[next_r][next_c] == 1:
                    dfs(next_r, next_c, grid)
            
        
        # loop through grid2
        # call dfs if grid1 == 0 but grid2 == 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid1[r][c] == 0 and grid2[r][c] == 1:
                    dfs(r,c,grid2)
        
        # loop through grid2
        # count num island remaining
        counter = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1:
                    dfs(r,c,grid2)
                    counter +=1
        return counter