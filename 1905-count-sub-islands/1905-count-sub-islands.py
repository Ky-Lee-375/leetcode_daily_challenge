class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def dfs(r, c, grid):
            grid[r][c] = 0
            
            for d in directions:
                new_r, new_c = r+d[0], c+d[1]
                if 0<= new_r < ROWS and 0<= new_c < COLS and grid[new_r][new_c] == 1:
                    dfs(new_r, new_c, grid)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid1[r][c] == 0 and grid2[r][c] == 1:
                    dfs(r,c,grid2)
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1:
                    dfs(r,c,grid2)
                    res += 1
        return res
            
        
        
        
        
    
    # clarifying 
    # completely overlap? still sub-island?
        