class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        island_area = {}
        island_id = 2
        visit = set()
        
        # give island id
        # dfs to find island area
        def dfs(r,c):
            area = 0
            stack = [(r,c)]
            while stack:
                r,c = stack.pop()
                if (r,c) in visit:
                    continue
                visit.add((r,c))
                
                area += 1
                grid[r][c]  = island_id
                
                for d in directions:
                    next_r, next_c = r + d[0], c + d[1]
                    if (0 <= next_r <ROWS) and (0 <= next_c <COLS) and grid[next_r][next_c] == 1:
                        area += dfs(next_r, next_c)
                        stack.append((next_r,next_c))
            return area
        
        # save it in dict
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    size = dfs(r,c)
                    island_area[island_id] = size
                    island_id += 2
                    
        max_size = max(island_area.values(), default=0)
        
        # go through the grid
        # find surr island
        # add to set
        # sum the negiboring island area
        
        for r in range(ROWS):
            for c in range(COLS):
                # find the empty land
                if grid[r][c] == 0:
                    area = 1
                    surr = set()
                    for d in directions:
                        next_r, next_c = r + d[0], c + d[1]
                        if (0 <= next_r < ROWS) and (0 <= next_c < COLS) and grid[next_r][next_c] > 1:
                            surr.add(grid[next_r][next_c])
                    for s in surr:
                        area += island_area[s]
                    max_size = max(max_size, area)
        return max_size
        
        # find the max sum