class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # row, col variable
        ROWS, COLS = len(grid), len(grid[0])
        # row, col, house list
        row, col, houses = [],[], []
        
        # iterate through the grid
        for r in range(ROWS):
            for c in range(COLS):
        # find the house
                if grid[r][c] == 1:
                    houses.append((r,c))
                    row.append(r)
        # add to the rwo and hourse list in a sorted order
        
        # do it col as well
        for c in range(COLS):
            for r in range(ROWS):
        # find the house
                if grid[r][c] == 1:
                    col.append(c)
                    
        # find the median
        # caculate dist from every hourse
        # return the sum of it
        median_r = row[len(row) // 2]
        median_c = col[len(col) // 2]
        
        res = 0
        for h in houses:
            res += abs(h[0]-median_r) + abs(h[1]-median_c)
        return res
        # clarifying question
        # return val: dist from every house
        # assume at least two houses always exist