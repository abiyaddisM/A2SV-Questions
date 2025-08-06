# August 5 2025
# https://leetcode.com/problems/coin-change-ii/description/
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        def helper(i, rem):
            if rem == 0:
                return 1
            if rem < 0:
                return 0
            if i >= len(coins):
                return 0
            if dp[i][rem] != -1:
                return dp[i][rem]

            take = helper(i, rem - coins[i])
            skip = helper(i + 1, rem)

            dp[i][rem] = take + skip
            return dp[i][rem]

        return helper(0, amount)
