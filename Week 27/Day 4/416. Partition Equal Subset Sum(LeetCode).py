# July 31 2025
# https://leetcode.com/problems/partition-equal-subset-sum/description/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dic = {}
        def helper(i, total):
            if total == target:
                return True
            if i >= len(nums):
                return False
            if (i, total) in dic:
                return dic[(i, total)]
            dic[(i, total)] = helper(i + 1, total) or helper(i + 1, total + nums[i])
            return dic[(i, total)]
        return helper(0, 0)
