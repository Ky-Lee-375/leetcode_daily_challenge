class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # variable
        ROWS, COLS = len(grid), len(grid[0])
        self.island_id = -1
        self.island_area = {}
        self.directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        
        # loop to update area dict and island id
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = self.dfs(grid, r, c)
                    self.island_area[self.island_id] = area
                    self.island_id -=1
        
        max_area = 0
        # loop through to find empty and add to surr
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    area = 1
                    surr = set()
                    
                    for d in self.directions:
                        next_r, next_c = r + d[0], c + d[1]
                        if (0 <= next_r < ROWS) and (0 <= next_c < COLS) and grid[next_r][next_c] != 0:
                            surr.add(grid[next_r][next_c])
                    for s_id in surr:
                        area += self.island_area[s_id]
                max_area = max(max_area, area) 
        return max_area if max_area else len(grid)**2
        
        
    def dfs(self, grid, r, c):
        ROWS, COLS = len(grid), len(grid[0])
        if (0<=r<ROWS) and (0<=c<COLS) and grid[r][c] ==1:
            grid[r][c] = self.island_id
            area = 1
            for d in self.directions:
                next_r, next_c = r + d[0], c + d[1]
                if (0 <= next_r < ROWS) and (0 <= next_c < COLS) and grid[next_r][next_c] ==1:
                    area += self.dfs(grid, next_r, next_c)
            return area
        else:
            return 0
        
        
        
        
        
        
        
        
        
        
        
        
        