# April 9 2025
# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        res = 0
        dic = {}
        total = 0
        l = 0
        for r in range(len(nums)):
            dic[nums[r]] = dic.get(nums[r], 0) + 1
            while len(dic) > k:
                dic[nums[l]] -= 1
                if dic[nums[l]] == 0:
                    dic.pop(nums[l])
                l += 1
                total = l
            while dic[nums[l]] > 1:
                dic[nums[l]] -= 1
                l += 1
            if len(dic) == k:
                res += (l - total) + 1

        return res