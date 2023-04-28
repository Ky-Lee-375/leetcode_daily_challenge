class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: que.append((i, j, 0))
        
        count = self.bfs(grid, que)
        
        for row in grid:
            for e in row:
                if e == 1: 
                    return -1
    
        return count
    
    def bfs(self, grid: List[List[str]], q: List[List[str]]) -> int:
        c = 0
        
        while q:
            i, j, d = q.pop(0)
            if d == 0 or grid[i][j] == 1:
                grid[i][j] = 2
                c = max(c, d)
                if i+1 < len(grid): 
                    q.append((i+1, j, d+1))
                if 0 <= i-1: 
                    q.append((i-1, j, d+1))
                if j+1 < len(grid[0]): 
                    q.append((i, j+1, d+1))
                if 0 <= j-1: 
                    q.append((i, j-1, d+1))

        return c