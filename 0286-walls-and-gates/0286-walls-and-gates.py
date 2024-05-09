class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # BFS + Queue
        # invoke BFS simultaneously
    
        # variable
        # ROW, COL
        # direction
        ROWS, COLS = len(rooms), len(rooms[0])
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        visit = set()
        q = deque()
        
        # go through the rooms
        # add all buildings (== 0)
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    visit.add((r,c))
                    q.append((r,c))
        
        # while queue
        # len of queue
            # add dist to grid
        # increment the dist
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = dist
                for d in directions:
                    next_r, next_c = r + d[0], c + d[1]
                    if (0 <= next_r <ROWS) and (0 <= next_c <COLS) and (next_r, next_c) not in visit and rooms[next_r][next_c] != -1:
                        visit.add((next_r, next_c))
                        q.append((next_r,next_c))
            dist += 1
                    
                    
                    
                    
                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    