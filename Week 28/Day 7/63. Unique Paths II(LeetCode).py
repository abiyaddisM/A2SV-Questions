# August 10 2025
# https://leetcode.com/problems/unique-paths-ii/description/
class Solution:
    def uniquePathsWithObstacles(self, og: List[List[int]]) -> int:
        n, m = len(og), len(og[0])
        dp = [ [0 for _ in range(m + 1)] for _ in range(n + 1)]
        dp[-1][-2] = 1 if og[-1][-1] == 0 else 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if og[i][j] == 1:
                    continue
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]


        return dp[0][0]
