# August 24 2025
# https://leetcode.com/problems/champagne-tower/description/
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0.0] * (query_row + 2)
        dp[0] = float(poured)

        for r in range(query_row):
            for j in range(r, -1, -1):
                overflow = max(0.0, dp[j] - 1.0)
                dp[j] = overflow / 2.0
                dp[j + 1] += overflow / 2.0

        return min(1.0, dp[query_glass])