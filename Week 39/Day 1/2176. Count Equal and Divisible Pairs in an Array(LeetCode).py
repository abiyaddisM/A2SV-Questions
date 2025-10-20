# October 20 2025
# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1
        return res
