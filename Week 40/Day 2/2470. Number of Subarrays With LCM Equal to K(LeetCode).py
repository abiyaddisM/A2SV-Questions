# October 28 2025
# https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            start = nums[i]
            for j in range(i, len(nums)):
                start = math.lcm(start, nums[j])
                if start == k:
                    res += 1


        return res