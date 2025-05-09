# May 9 2025
# https://leetcode.com/problems/subarray-product-less-than-k/description/
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        res = 0
        total = 1
        l = 0
        for r in range(len(nums)):
            total = total * nums[r]
            while l <= r and total >= k:
                total = total // nums[l]
                l += 1
            res += r - l + 1
        return res
