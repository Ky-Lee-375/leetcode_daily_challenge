class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        island_size = {}
        island_id = 2  # Start from 2 since 0 and 1 are already used in the grid
        
        def dfs(r, c):
            stack = [(r, c)]
            size = 0
            while stack:
                x, y = stack.pop()
                if (x, y) in seen:
                    continue
                seen.add((x, y))
                grid[x][y] = island_id
                size += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 1:
                        stack.append((nx, ny))
            return size

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        seen = set()
        
        # Identify all islands and calculate their sizes
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    size = dfs(r, c)
                    island_size[island_id] = size
                    island_id += 1
        
        # If no '0' is found, return the size of any island (all are '1's)
        max_size = max(island_size.values(), default=0)
        
        # Check all '0's and calculate the possible maximum island size by connecting adjacent islands
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    possible_island = 1
                    unique_islands = set()
                    for dx, dy in directions:
                        nx, ny = r + dx, c + dy
                        if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] > 1:
                            unique_islands.add(grid[nx][ny])
                    possible_island += sum(island_size[id] for id in unique_islands)
                    max_size = max(max_size, possible_island)
        
        return max_size