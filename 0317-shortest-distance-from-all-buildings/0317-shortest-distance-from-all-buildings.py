class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dist_matrix = [[0]*cols for _ in range(rows)]
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        BUILDING = 1
        OBSTACLE = 2
        EMPTY = 0
        
        min_dist = float('inf')
        
        # BFS + queue
        # if empty land is found, add to queue
        # recursive BFS to neighbor node
        
        for row in range(rows):
            for col in range(cols):
                # if building is found
                # call recusive dfs
                if grid[row][col] == BUILDING:
                    local_dist = float('inf')
                    queue = collections.deque([(row, col, 0)])

                    while queue:
                        cur_row, cur_col, dist = queue.popleft()
                        for d in directions:
                            next_row, next_col = cur_row + d[0], cur_col + d[1]
                            if (0 <= next_row < rows) and (0 <= next_col<cols) and grid[next_row][next_col] == EMPTY:
                                grid[next_row][next_col] -= 1
                                dist_matrix[next_row][next_col] += dist + 1
                                
                                queue.append((next_row, next_col, dist+1))
                                local_dist = min(local_dist, dist_matrix[next_row][next_col])
                    EMPTY -= 1
                    min_dist = local_dist
        return min_dist if min_dist != float('inf') else -1
        