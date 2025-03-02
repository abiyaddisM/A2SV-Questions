# March 2 2025
# https://leetcode.com/problems/maximum-erasure-value/
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        total = nums[0]
        ms = {nums[0]}
        res = total
        l = 0
        for r in range(1,len(nums)):
            while nums[r] in ms:
                total -= nums[l]
                ms.discard(nums[l])
                l += 1
            total += nums[r]
            ms.add(nums[r])
            res = max(total,res)
        return res