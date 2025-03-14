# March 14 2025
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
class Solution:
    def countPairs(self, nums: List[int], t: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = 0
        while l < r:
            while l < r and nums[l] + nums[r] >= t:
                r -= 1
            res += r - l
            l += 1

        return res