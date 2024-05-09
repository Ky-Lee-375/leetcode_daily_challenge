class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # variable: row, col, directions
        # island dict
        # island id
        ROW, COL = len(grid), len(grid[0])
        self.directions = [(0,1), (0,-1), (1,0), (-1,0)]
        self.island_area = {}
        self.island_id = -1
        
        # find island 
        # update the island dict w island size
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = self.dfs(grid, r,c)
                    self.island_area[self.island_id] = area
                    self.island_id -=1
        
        # find empty land
        # find surrounding island
        # sum the surrounding
        max_area =0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    area = 1
                    surr = set()
                    for d in self.directions:
                        next_r, next_c = r + d[0], c+ d[1]
                        if (0<=next_r<ROW) and (0 <= next_c <COL) and grid[next_r][next_c] != 0:
                            surr.add(grid[next_r][next_c])
                    for s_id in surr:
                        area += self.island_area[s_id]
                max_area = max(max_area, area)
        return max_area if max_area else len(grid)**2
        # dfs: class function
        # grid, r, c
        # find the island 
        # update the grid w island id
        # return the size of island
    def dfs(self, grid, r,c):
        ROW, COL = len(grid), len(grid[0])
        if (0<=r<ROW) and (0<=c<COL) and grid[r][c] == 1:
            grid[r][c] = self.island_id
            area = 1
            for d in self.directions:
                next_r, next_c = r + d[0], c+d[1]
                if (0<=next_r<ROW) and (0<=next_c<COL) and grid[next_r][next_c] == 1:
                    area += self.dfs(grid, next_r, next_c)
            
            return area
        else:
            return 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        