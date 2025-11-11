# November 11 2025
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
class Solution:
    def subsetXORSum(self, nums):
        total_or = 0
        for x in nums:
            total_or |= x
        return total_or * (1 << (len(nums) - 1))