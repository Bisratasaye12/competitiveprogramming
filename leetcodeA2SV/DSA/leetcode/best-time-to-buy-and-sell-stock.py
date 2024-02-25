class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mx = 0
        profit = 0

        for i in range(n-1, -1, -1):

            profit = max(profit, mx - prices[i])
            mx = max(mx, prices[i])

        return profit