class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # sort and zip by difficulty
        jobs = sorted(zip(difficulty, profit))
        worker = sorted(worker)
        
        # find the highest difficulty a worker can do
        cur = j = profit = 0
        for i in range(len(worker)):
            while j < len(jobs) and worker[i] >= jobs[j][0]:
                cur = max(cur, jobs[j][1])
                j += 1
            profit += cur
        return profit
        