# August 21 2025
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        hold = float('-inf')
        sold = 0
        rest = 0
        for p in prices:
            ph, ps, pr = hold, sold, rest
            hold = max(ph, pr - p)
            sold = ph + p
            rest = max(pr, ps)
        return max(sold, rest)