# April 13 2025
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        ma = nums[0]
        comp = nums[0]
        res = 0
        for i in range(1,len(nums)):
            if nums[i] < comp:
                res = i
                comp = ma
            ma = max(nums[i], ma)
        res += 1
        return res