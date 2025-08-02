# August 2 2025
# https://leetcode.com/problems/longest-increasing-subsequence/description/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n + 2) for _ in range(n + 2)]

        def helper(i, pre):
            if i >= n:
                return 0
            if memo[i][pre] != -1:
                return memo[i][pre]
            include = 0

            if pre == -1 or nums[i] > nums[pre]:
                include = 1 + helper(i + 1, i)
            exclude = helper(i + 1, pre)
            memo[i][pre] = max(exclude, include)
            return memo[i][pre]

        return helper(0, -1)