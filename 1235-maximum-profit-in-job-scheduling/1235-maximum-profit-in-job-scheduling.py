class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # zip the values and sort by startTime
        intervals = sorted(zip(startTime, endTime, profit))
        
        # cache
        cache = {}
        
        # dfs
        def dfs(i):
            # base case: last job 
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
                
            # Don't include
            res = dfs(i+1)
            
            # Include
                # binary search to find the next start time
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = res = max(res, intervals[i][2] +dfs(j))
            return res
        
        # return max profit
        return dfs(0)
      
            
            