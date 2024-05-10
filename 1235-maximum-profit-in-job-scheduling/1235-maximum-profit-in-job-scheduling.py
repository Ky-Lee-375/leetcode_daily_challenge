class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # variable declaration
        # cache -> optimize
        # sort & zip the variable
        jobs = sorted(zip(startTime, endTime, profit))
        cache = {}
        # dfs(job_id)
        # if the job is the last -> return 0
        # return the max

        def dfs(i):
            if i == len(jobs):
                return 0
            if i in cache:
                return cache[i]
            # not take -> next job
            profit = dfs(i+1)

            # take -> binary seach next searchtime
            idx = bisect.bisect_left(jobs, (jobs[i][1], -1, -1))
            cache[i] = profit = max(profit, jobs[i][2] + dfs(idx))
            
            return profit
        
        return dfs(0)
        