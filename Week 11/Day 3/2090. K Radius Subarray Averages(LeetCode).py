# April 9 2025
# https://leetcode.com/problems/k-radius-subarray-averages/description/
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1 for _ in range(k)]
        if math.ceil(len(nums) / 2) < k:
            return [-1 for _ in range(len(nums))]
        total = 0
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            if r >= (k * 2):
                res.append(total  // (r - l + 1))
                total -= nums[l]
                l += 1
        for i in range(k):
            res.append(-1)
        return res