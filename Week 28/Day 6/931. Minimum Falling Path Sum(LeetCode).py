# August 9 2025
# https://leetcode.com/problems/minimum-falling-path-sum/description/
class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        dp = mat[-1][:]

        for i in range(n - 2, -1, -1):
            new = [0] * n
            for j in range(n):
                best = dp[j]
                if j > 0:
                    best = min(best, dp[j - 1])
                if j + 1 < n:
                    best = min(best, dp[j + 1])
                new[j] = mat[i][j] + best
            dp = new

        return min(dp)