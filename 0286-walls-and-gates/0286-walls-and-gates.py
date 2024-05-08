class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visit = set()
        q = deque()
        
        # add gates to queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    visit.add((r,c))
                    q.append((r,c))
        
        # BFS
        # invoke BFS from every gate
        # add to queue
        # for the length of queue, recursive call
        # increment the dist
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                
                for d in directions:
                    next_row, next_col = r + d[0], c + d[1]
                    if (0 <= next_row < rows) and (0 <= next_col < cols) and (next_row, next_col) not in visit and rooms[next_row][next_col] != -1:
                        visit.add((next_row, next_col))
                        q.append((next_row, next_col))
            dist += 1
    
            
        