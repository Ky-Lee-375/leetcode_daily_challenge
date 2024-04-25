class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # initialize variables
        # row, col, direction, queue
        ROWS, COLS = len(rooms), len(rooms[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque()
        visit = set()
        
        # add gates to queue
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        # while queue exists
        # bfs with queue
        # pop the item and call bfs recursive
        # increment dist after poping everything in the same level
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                for d in directions:
                    next_r, next_c = r+d[0], c + d[1]
                    if 0<=next_r< ROWS and 0<=next_c< COLS and rooms[next_r][next_c] != -1 and (next_r, next_c) not in visit:
                        q.append((next_r, next_c))
                        visit.add((next_r, next_c))
            dist += 1
                            
                        
        
        