class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # edge case
        if min(difficulty) > max(worker):
            return 0
        
        # zip difficulty and profit
        # sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        print(jobs)
        curr = j = res = 0
        worker = sorted(worker)
        for i in range(len(worker)):
            while j < len(jobs) and jobs[j][0] <= worker[i]:
                curr = max(curr, jobs[j][1])
                j += 1
            res += curr        
        return res
            