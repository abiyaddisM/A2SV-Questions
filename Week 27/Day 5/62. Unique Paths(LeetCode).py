# August 1 2025
# https://leetcode.com/problems/unique-paths/description/
class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        dic = {}

        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m

        def helper(i, j):
            if not inbound(i, j):
                return 0
            if i == n - 1 and j == m - 1:
                return 1
            if (i, j) in dic:
                return dic[(i, j)]

            dic[(i, j)] = helper(i + 1, j) + helper(i, j + 1)
            return dic[(i, j)]

        return helper(0, 0)