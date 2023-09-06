class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = prices[0]
        benefit = 0
        for i in range(1, len(prices)):
            if prices[i]-price > benefit:
                benefit = prices[i]-price
            if prices[i] < price:
                price = prices[i]
        return benefit