# February 7 2025
# https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/description/
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i - 1])
        res = []
        val = 0
        for i in range(len(nums) + 1):
            total = 0
            if i != 0:
                total += i - prefix[i - 1]
            if i != len(nums):
                total += prefix[-1] - (prefix[i - 1] if i != 0 else 0)
            if len(res) == 0 or val == total:
                res.append(i)
                val = total
            elif total > val:
                res = [i]
                val = total


        return res