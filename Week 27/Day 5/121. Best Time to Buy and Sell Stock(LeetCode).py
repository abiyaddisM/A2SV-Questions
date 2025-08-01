# August 1 2025
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        anchor,checker = 0,0

        total = 0

        size = len(prices)

        while checker < size:

            sum = prices[checker] - prices[anchor]

            if sum < 0:

                anchor = checker

            else:

                total = sum if sum > total else total

            checker += 1

        return total