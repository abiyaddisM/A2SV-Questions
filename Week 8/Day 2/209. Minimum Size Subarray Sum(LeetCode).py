# March 18 2025
# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        total = 0
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res,(r - l) + 1)
                total -= nums[l]
                l += 1
        print(not res)
        return res if res < float('inf') else 0