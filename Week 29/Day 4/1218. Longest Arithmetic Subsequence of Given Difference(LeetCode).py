# August 14 2025
# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/
class Solution:
    def longestSubsequence(self, arr: List[int], di: int) -> int:
        dp = {}
        best = 0
        for v in arr:
            dp[v] = dp.get(v - di, 0) + 1
            best = max(best, dp[v])
        return best