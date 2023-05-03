class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        
        if s < target: return 0

        dp = [[0] * (2 * s + 1) for _ in range(n + 1)]
        dp[0][s] = 1

        for i in range(n):
            for j in range(nums[i], 2 * s + 1 - nums[i]):

                if dp[i][j]:
                    dp[i + 1][j + nums[i]] += dp[i][j]
                    dp[i + 1][j - nums[i]] += dp[i][j]

        return dp[-1][s + target]