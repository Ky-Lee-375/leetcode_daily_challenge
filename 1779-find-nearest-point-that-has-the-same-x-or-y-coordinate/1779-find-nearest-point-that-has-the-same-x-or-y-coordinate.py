class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        n = len(points)
        hashmap = {}
        
        for i in range(n):
            if points[i][0] == x or points[i][1] == y:
                dist = abs(x-points[i][0]) + abs(y - points[i][1])
                if dist in hashmap:
                    hashmap[dist] = min(hashmap[dist], i)
                else:
                    hashmap[dist] = i
        print(hashmap)
        res = -1
        if hashmap:
            res = hashmap[min(hashmap.keys())]
        return res
                
    
    # clarifying
        # return the index of valid point w smallest dist
            # otherwise return -1
        # Can I assume points list always exsit?
    
    # algorithm
    # hashmap (dist, [index])
    # return min idx of min dist