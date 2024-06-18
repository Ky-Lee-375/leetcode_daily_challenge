class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # use hashmap
        N = len(points)
        hashmap = {}
        
        # valid if it shares x or y loc
        # if valid, find the dist and store the index
        for i in range(N):
            if points[i][0] == x or points[i][1] == y:
                dist = abs(points[i][0] - x) + abs(points[i][1] - y)
                if dist in hashmap:
                    hashmap[dist] = min(hashmap[dist], i)
                else:
                    hashmap[dist] = i
        # return the idx of the smallest distance point
        res = -1
        if hashmap:
            res = hashmap[min(hashmap.keys())]
        return res