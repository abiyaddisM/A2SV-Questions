# August 5 2025
# https://leetcode.com/problems/jump-game-ii/description/
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}

        def helper(i):
            if i >= len(nums) - 1:
                return 0
            if i in dp:
                return dp[i]
            temp = len(nums)
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                temp = min(temp, 1 + helper(j))
            dp[i] = temp
            return dp[i]

        return helper(0)