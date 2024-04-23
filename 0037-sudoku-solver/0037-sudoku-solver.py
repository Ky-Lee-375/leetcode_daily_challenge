class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # consider 3x3
        squares = collections.defaultdict(set)
        # consider row
        rows = collections.defaultdict(set)
        # consider column
        cols = collections.defaultdict(set)
        
        # update the current state
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                num = int(board[r][c])
                rows[r].add(num)
                cols[c].add(num)
                squares[(r//3)*3 + c//3].add(num)
                
        def isValid(r,c,v):
            box_id = (r//3)*3 + c//3
            return v not in rows[r] and v not in cols[c] and v not in squares[box_id]
        
        def backtrack(r,c):
            if r == 8 and c == 9:
                return True
            elif c==9:
                r += 1
                c = 0
            
            if board[r][c] != '.':
                return backtrack(r, c+1)
            box_id = (r//3) * 3 + c//3
            for v in range(1, 10):
                if not isValid(r, c, v):
                    continue
                board[r][c] = str(v)
                rows[r].add(v)
                cols[c].add(v)
                squares[box_id].add(v)
                
                if backtrack(r, c+1):
                    return True
                
                # revert back 
                board[r][c] = '.'
                rows[r].remove(v)
                cols[c].remove(v)
                squares[box_id].remove(v)
            return False
        backtrack(0,0)
            
        
        # backtracking problem
        