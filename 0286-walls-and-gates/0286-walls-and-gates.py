class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # initialize ROWS and COLS
        ROWS, COLS = len(rooms), len(rooms[0])
        # queue to keep track of loc
        q = deque()
        # visit set
        visit = set()
        # directions or helper function
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        # add all gates to queue
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        # if queue exists:
        while q:
        # pop the value
            for i in range(len(q)):
                r,c = q.popleft()
                # assign dist to the loc
                rooms[r][c] = dist
                # move to available direction
                for d in directions:
                    next_r, next_c = r + d[0], c + d[1]
                    if  0 <= next_r < ROWS and 0 <= next_c < COLS and (next_r, next_c) not in visit and rooms[next_r][next_c] != -1:
                        q.append((next_r, next_c))
                        visit.add((next_r, next_c))
                
            dist += 1
                
        
       
        
        # clarifying questions:
            # is it possible to not have any gates? == only walls?
            # direction -> no diagonal?
            # no return value?
        
        # algorithms
            # bfs
            # using dist variable start from 0 at gate
            # invoke simultaneous call from every gate
            # increment the distance after finding all distance
            