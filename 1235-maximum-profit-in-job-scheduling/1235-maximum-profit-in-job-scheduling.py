class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # zip the variable
        intervals = sorted(zip(startTime, endTime, profit))
        # cache
        cache = {}
        
        # dfs + binary search
            # don't take
            # move to the next
            # take -> find the next start
        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            
            res = dfs(i+1)
            
            next_j = bisect.bisect_left(intervals, (intervals[i][1], -1,-1))
            cache[i] = res = max(res, intervals[i][2] + dfs(next_j))
            return res
        
        # return max
        return dfs(0)