# July 30 2025
# https://leetcode.com/problems/house-robber/description/
class Solution:
    def rob(self, nums: List[int]) -> int:
        dic = {}
        def helper(i):
            if i >= len(nums):
                return 0
            if i in dic:
                return dic[i]
            t1 = nums[i] + helper(i + 2)
            t2 = helper(i + 1)
            dic[i] = max(t1,t2)
            return max(t1, t2)

        return helper(0)