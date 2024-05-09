class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # variable declaration
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        # maintain dist matrix
        dist_matrix = [[0]*COLS for _ in range(ROWS)]
        
        BUILDING = 1
        OBSTACLE = 2
        EMPTY = 0
        
        # final min dist
        min_dist = float('inf')
        
        # bfs
        # everytime we traverse from one building, decrement
        # update the dist matrix
        # when we are done traversing, find the min from dist matrix
        for row in range(ROWS):
            for col in range(COLS):
                # local distance 
                local_dist = float('inf')
                # if building, add to queue
                if grid[row][col] == BUILDING:
                    q = collections.deque([(row,col,0)])
                
                    # while queue
                    # pop the item
                    # move to 4 directions
                    # update the distance
                        # update dist_matrix (+=)
                        # mark original grid -=1
                    while q:
                        cur_r, cur_c, dist = q.popleft()
                        for d in directions:
                            next_r, next_c = cur_r + d[0], cur_c + d[1]
                            if (0 <= next_r < ROWS) and (0 <= next_c < COLS) and grid[next_r][next_c] == EMPTY:
                                grid[next_r][next_c] -= 1
                                dist_matrix[next_r][next_c] += dist + 1

                                # add the next to the queue
                                # update the local dist
                                q.append((next_r, next_c, dist+1))
                                local_dist = min(local_dist, dist_matrix[next_r][next_c])
                    # update empty
                    EMPTY -= 1
                    min_dist = local_dist
        return min_dist if min_dist != float('inf') else -1
                