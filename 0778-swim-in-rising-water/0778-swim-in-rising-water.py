class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijikstra + heap
        # min heap (height, r, c)
        # visit set
        # direction
        ROW, COL = len(grid), len(grid[0])
        minH = [[grid[0][0], 0, 0]]
        visit = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        # start from (0,0)
        # add to visit set
        visit.add((0,0))
        
        # while heap
        # pop from heap
        # if it's the right bottom grid, just return the height
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == ROW-1 and c == COL-1:
                return t
              
            # if not, move 4 directions
            # find the max
                # add to visit set
                # heap push
            for d in directions:
                next_r, next_c = r + d[0], c + d[1]
                if (0<=next_r < ROW) and (0 <= next_c < COL) and (next_r, next_c) not in visit:
                    visit.add((next_r,next_c))
                    heapq.heappush(minH, [max(t, grid[next_r][next_c]), next_r, next_c])
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
