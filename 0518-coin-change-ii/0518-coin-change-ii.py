class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for n in range(amount - coin + 1):
                dp[n + coin] += dp[n]
        return dp[amount]