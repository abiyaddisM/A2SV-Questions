# August 4 2025
# https://leetcode.com/problems/edit-distance/description/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][-1] = n - i
        for j in range(m + 1):
            dp[-1][j] = m - j

        def helper(i, j):
            if not (i < n and j < m):
                return dp[i][j]
            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = helper(i + 1, j + 1)
            else:
                t1 = 1 + helper(i + 1, j)
                t2 = 1 + helper(i, j + 1)
                t3 = 1 + helper(i + 1, j + 1)
                dp[i][j] = min([t1, t2, t3])

            return dp[i][j]

        return helper(0, 0)