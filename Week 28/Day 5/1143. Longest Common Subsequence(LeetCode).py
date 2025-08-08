# August 8 2025
# https://leetcode.com/problems/longest-common-subsequence/description/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def helper(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + helper(i + 1, j + 1)
            else:
                dp[(i, j)] = max(helper(i + 1, j), helper(i, j + 1))
            return dp[(i, j)]

        return helper(0, 0)
