class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # zip the variable so that I can keep track
        # sort by startTime
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        
        # recursive DFS
        # two approach: 1) not take the job 2) take it and find the next one
        def dfs(i):
            # base case: if it reaches the end
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            
            # 1) not take the job
            res = dfs(i+1)
            
            # 2) take the job
            # binary search
            idx = bisect.bisect_left(intervals, (intervals[i][1], -1,-1))
            cache[i] = res = max(res, intervals[i][2]+ dfs(idx))
            return res
        
        return dfs(0)
        
        
        