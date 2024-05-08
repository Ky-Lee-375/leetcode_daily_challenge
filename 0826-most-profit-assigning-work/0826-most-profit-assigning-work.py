class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        if min(difficulty) > max(worker):
            return 0
        
        jobs = sorted(zip(difficulty, profit))
        worker = sorted(worker)
        
        cur = j = res = 0
        for i in range(len(worker)):
            while j < len(jobs) and worker[i] >= jobs[j][0]:
                cur = max(cur, jobs[j][1])
                j += 1
            res += cur
        return res
            
        