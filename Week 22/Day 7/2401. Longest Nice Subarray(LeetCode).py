# June 28 2025
# https://leetcode.com/problems/longest-nice-subarray/description/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        l = 0
        bitmask = 0

        for r in range(len(nums)):
            while (bitmask & nums[r]) != 0:
                bitmask ^= nums[l]
                l += 1
            bitmask |= nums[r]
            res = max(res, r - l + 1)

        return res
