class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # var
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        # dfs
        def dfs(r,c):
            if (r < 0) or (r == ROWS) or (c < 0) or (c == COLS) or ((r,c) in visit) or (grid[r][c] == 0):
                return 0
            visit.add((r,c))
            return (1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1)+ dfs(r, c+1))
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))
        return area                
        
        