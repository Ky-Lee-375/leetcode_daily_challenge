class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        # invoke BFS on every gate
        # increase the depth after one iteration
        # use queue to initially store the gate
        
        # variable declaration
        ROWS, COLS = len(rooms), len(rooms[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque()
        visit = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = dist
                
                for dr, dc in directions:
                    next_r, next_c = r+dr, c + dc
                    if (0 <= next_r < ROWS) and (0<=next_c<COLS) and rooms[next_r][next_c] != -1 and (next_r, next_c) not in visit:
                        visit.add((next_r,next_c))
                        q.append((next_r,next_c))
            dist+=1
        
        