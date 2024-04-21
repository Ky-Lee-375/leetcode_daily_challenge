class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # base case check
            # min diff > max worker
            # return 0
        if min(difficulty) > max(worker):
            return 0
        # zip diff and profit
        jobs = sorted(zip(difficulty, profit))
        
        best = max_profit = j_idx = 0
        for w in sorted(worker):
            while j_idx < len(jobs)  and w >= jobs[j_idx][0]:
                best = max(best, jobs[j_idx][1])
                # print("best " + str(best))
                j_idx += 1
            max_profit += best
            # print(max_profit)
        return max_profit
        # search max lowest val for each worker
            # binary search
            # add profit to total profit
        # return profit
        
        