# July 27 2025
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        count = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1
            res = max(res, r - l + 1)
        return res