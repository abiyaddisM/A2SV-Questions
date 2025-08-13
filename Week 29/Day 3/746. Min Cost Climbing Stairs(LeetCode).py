# August 13 2025
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}

        def helper(i):
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = min(cost[i] + helper(i + 1), cost[i] + helper(i + 2))
            return dp[i]

        return min(helper(0), helper(1))