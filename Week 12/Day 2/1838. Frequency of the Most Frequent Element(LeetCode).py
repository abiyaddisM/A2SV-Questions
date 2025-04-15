# April 15 2025
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        total = 0
        l = 0
        for r in range(1,len(nums)):
            total += (nums[r] - nums[r - 1]) * (r - l)
            while total > k:
                total -= nums[r] - nums[l]
                l += 1
            res = max(res,r - l + 1)

        return res