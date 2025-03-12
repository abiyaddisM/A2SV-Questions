# March 12 2025
# https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = 0
        while l < r:
            total = nums[l] + nums[r]
            if total > k:
                r -= 1
            elif total < k:
                l += 1
            else:
                res += 1
                l += 1
                r -= 1
        return res