class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # zip difficulty and profit
        # sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        worker = sorted(worker)
        
        # sort worker array
        # while loop
        # find the max diff per worker
        cur = j = res = 0
        for i in range(len(worker)):
            w = worker[i]
            while j < len(jobs) and w >= jobs[j][0]:
                cur = max(cur, jobs[j][1])
                j+=1
            res += cur
        # add the profit
        # return the profit
        return res