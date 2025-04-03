# April 3 2025
# https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res = 0
        dic = {}
        total = 0
        l = 0
        for r in range(len(nums)):
            dic[nums[r]] = dic.get(nums[r], 0) + 1
            total += dic[nums[r]] - 1
            res += l
            while total >= k:
                res += 1
                total -= dic[nums[l]] - 1
                dic[nums[l]] -= 1
                l += 1
        return res