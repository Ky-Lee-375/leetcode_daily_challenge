class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        row, col, houses = [], [], []
        
        # add the point in order
        # do one for row
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row.append(r)
                    houses.append((r,c))
                
        # one for col
        for c in range(COLS):
            for r in range(ROWS):
                if grid[r][c] == 1:
                    col.append(c)
        
        # mid point
        # mid from col and row
        mid_r = row[len(row)//2]
        mid_c = col[len(col)//2]
        
        dist = 0
        for hr, hc in houses:
            dist += abs(hr-mid_r) + abs(hc-mid_c)
        return dist
        