# February 4 2025
# https://leetcode.com/problems/maximum-product-of-three-numbers/description/
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = max(nums[0] * nums[1] * nums[2], nums[0] * nums[-1] * nums[-2])
        return res

