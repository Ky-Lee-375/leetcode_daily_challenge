class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        # island dict
        island_size = {}
        # give isalnd id
        island_id =2
        # use dfs to find island area
        
        visit = set()
        # dfs (r,c)
        def dfs(r,c):
            size = 0
            stack = [(r,c)]
            while stack:
                r,c = stack.pop()
                if (r,c) in visit:
                    continue
                visit.add((r,c))
                # assign island id
                grid[r][c] = island_id
                size += 1
                for d in directions:
                    next_r, next_c = r + d[0], c+d[1]
                    if 0<=next_r < ROWS and 0 <= next_c < COLS and grid[next_r][next_c] == 1:
                        # find the island
                        stack.append((next_r, next_c))
            # return the island area
            return size
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    size = dfs(r,c)
                    island_size[island_id] = size
                    island_id += 1
        max_size = max(island_size.values(), default=0)
        
        # iterate over the grid
        # find 0 -> add +1 to area
        # find the surrounding island
        # add the area of surrounding
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    area = 1
                    surr = set()
                    for d in directions:
                        next_r, next_c = r+d[0], c + d[1]
                        if 0<=next_r<ROWS and 0 <= next_c<COLS and grid[next_r][next_c] > 1:
                            surr.add(grid[next_r][next_c])
                    for s in surr:
                        area += island_size[s]
                    max_size = max(max_size, area)
        return max_size
        
    
    # algorithm
    # dfs
    # maintain visit set or smth like that
    # keep track of max island size and idx (r,c)
    # put locations of all 0 in queue
    # start from (0,0) -> check 4 directions
        # if all 4 is 1, then move on 
        # 
    
    
    
    
    
    
    
    
    # clarify
    # return: size of the larges island in grid
    # change only one 0 to be 1
        # can decide not to change?
    # island: no diagonal with 1s