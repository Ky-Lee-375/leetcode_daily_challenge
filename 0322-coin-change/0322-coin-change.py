class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
    
        # Base case: it takes 0 coins to make up amount 0
        dp[0] = 0

        # Iterate through all amounts from 1 to amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still float('inf'), it means it's not possible to make up the amount
        return dp[amount] if dp[amount] != float('inf') else -1
        
        