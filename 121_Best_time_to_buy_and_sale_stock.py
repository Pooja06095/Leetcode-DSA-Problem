class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit(prices))