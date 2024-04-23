class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        
        # Initialize BFS from the starting point '*'
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '*':
                    queue.append((r, c, 0))  # Store (row, col, distance) in the queue
                    visited.add((r, c))
                    break

        # Directions array for moving in 4 possible directions (N, E, S, W)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c, dist = queue.popleft()
            
            # Check if we've found a food cell
            if grid[r][c] == '#':
                return dist
            
            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] != 'X':
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
        return -1
