class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # zip the value
        # sort the data
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        
        # recursive dfs
        def dfs(i):
            if len(intervals) == i:
                return 0
            # check cache
            if i in cache:
                return cache[i]
        # compare not include vs include -> find max
            # not include
            res = dfs(i+1)
            
            # include
            # find the next start time
            next_job = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = res = max(res, intervals[i][2] + dfs(next_job))
            return res
        # call dfs on the first one
        return dfs(0)
      
            
            