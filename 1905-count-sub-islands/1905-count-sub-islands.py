class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        counter = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        # dfs(r,c,grid)
        # from r,c change all 1 to 0
        def dfs(r,c, grid):
            grid[r][c] = 0
            
            for d in directions:
                next_r, next_c = r + d[0], c + d[1]
                if (0<=next_r<ROWS) and (0 <= next_c < COLS) and grid[next_r][next_c] == 1:
                    dfs(next_r, next_c, grid)
        
        # if 0 in grid 1 and 1 in grid 2 -> can't be sub island
        # call dfs
        for r in range(ROWS):
            for c in range(COLS):
                if grid1[r][c] == 0 and grid2[r][c] == 1:
                    dfs(r,c,grid2)
        
        # everytime we see 1
        # call dfs
        # increment the counter
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] ==1:
                    dfs(r,c,grid2)
                    counter += 1
        return counter
        