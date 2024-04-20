class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        
        def dfs(i):
            # run out of interval
            if i == len(intervals):
                return 0
            # if already computed,return the cache
            if i in cache:
                return cache[i]
            
            # dont include
            res = dfs(i+1)
            # include
            # binary seach the next job
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return res
        return dfs(0)
            
            
            