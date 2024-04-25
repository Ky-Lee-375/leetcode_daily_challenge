class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # zip the input
        # sort by start time O(n logn)
        intervals = sorted(zip(startTime, endTime, profit))
        # intervals.sort(key = lambda x:x[0])
        cache = {}
        
        # cache
        
        # dfs(idx) + binary search 
        # find the next start time using the end time of current job
        # 1. include
        # 2. not include
        # keep track of max
        def dfs(idx):
            profit = 0
            if idx == len(intervals):
                return 0
            if idx in cache:
                return cache[idx]
            
            # don't take
            # call dfs on next
            profit = dfs(idx+1)

            # take
            # find the next start time
            next_j = bisect.bisect(intervals, (intervals[idx][1], -1, -1))
            cache[idx] = profit = max(profit, intervals[idx][2] + dfs(next_j))
            return profit
        
        return dfs(0)
        