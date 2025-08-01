# August 1 2025
# https://leetcode.com/problems/target-sum/description/
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic ={}

        def helper(i, total):
            if i >= len(nums):
                return int(total == target)
            if (i, total) in dic:
                return dic[(i, total)]
            dic[(i, total)] = helper(i + 1,total - nums[i]) + helper(i + 1,total + nums[i])
            return dic[(i, total)]

        return helper(0, 0)