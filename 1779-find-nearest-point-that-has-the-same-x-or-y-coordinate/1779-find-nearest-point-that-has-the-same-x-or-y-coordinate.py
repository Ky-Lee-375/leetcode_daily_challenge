class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        if len(points) == 0:
            return -1
        if len(points) == 1 and (x == points[-1][0] and y == points[-1][1]):
            return 0

        rest = float('inf')
        idx = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                dist = abs(x - points[i][0] )  + abs(y - points[i][1])
                if dist < rest:
                    rest = dist
                    idx = i
        return idx
                
        
            
        