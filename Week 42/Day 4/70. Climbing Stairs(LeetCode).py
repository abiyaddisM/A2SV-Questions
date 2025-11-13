# November 13 2025
# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n: int) -> int:

        dic = {}

        def dp(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in dic:
                return dic[i]
            dic[i] = dp(i + 1) + dp(i + 2)
            return dic[i]

        return dp(0)