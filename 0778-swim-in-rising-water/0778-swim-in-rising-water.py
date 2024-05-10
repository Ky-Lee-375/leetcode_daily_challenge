class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # variable
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (0,-1),(1,0), (-1,0)]
        # minheap (grid[r][c], r, c)
        # visit set
        minHeap = [[grid[0][0], 0, 0]]
        visit = set()
        
        visit.add((0,0))
        # loop through the grid
        # if row, col is bottom right, return time
        for r in range(ROWS):
            for c in range(COLS):
                t,r,c = heapq.heappop(minHeap)
                if r == ROWS-1 and c == COLS-1:
                    return t
                
                for d in directions:
                    next_r, next_c = r + d[0], c + d[1]
                    if (0 <= next_r <ROWS) and (0 <= next_c < COLS) and (next_r, next_c) not in visit:
                        heapq.heappush(minHeap, [max(t, grid[next_r][next_c]), next_r, next_c])
                        visit.add((next_r, next_c))
        