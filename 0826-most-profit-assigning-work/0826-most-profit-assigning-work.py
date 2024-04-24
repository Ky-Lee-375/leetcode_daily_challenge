class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # edge case
        if min(difficulty) > max(worker):
            return 0
        jobs = sorted(zip(difficulty, profit))
        
        worker = sorted(worker)
        max_profit = curr_prof = j = 0

        
        for i in range(len(worker)):
            while j < len(jobs) and jobs[j][0] <= worker[i]:
                curr_prof = max(curr_prof, jobs[j][1])
                j += 1
            max_profit += curr_prof
        return max_profit