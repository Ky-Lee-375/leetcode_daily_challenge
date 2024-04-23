class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # keep track of rows, cols, square
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        # iterate through the board
        for r in range(9):
            for c in range(9):
                # no value in here -> continue
                if board[r][c] == '.':
                    continue
                # check if seen in any of the structure
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
        
        