# March 28 2025
# https://leetcode.com/problems/array-partition/description/
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) // 2):
            res += min(nums[i * 2], nums[i * 2 + 1])

        return res