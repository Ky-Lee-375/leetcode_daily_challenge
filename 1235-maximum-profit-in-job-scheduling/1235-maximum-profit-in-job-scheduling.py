class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort & zip
        intervals = sorted(zip(startTime, endTime, profit))
        # cache / memoization
        cache = {}
        profit = 0
        
        # dfs
        def dfs(i):
        # keep track of max profit
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            # Don't take -> take the next
            profit = dfs(i+1)
            
            # take -> find the next starting using binary search
            next_idx = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            # call bfs on the next item
            
            cache[i] = profit = max(profit, intervals[i][2] + dfs(next_idx))
            return profit
        
        return dfs(0)
                    
        