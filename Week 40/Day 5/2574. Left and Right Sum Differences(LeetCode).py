# October 31 2025
# https://leetcode.com/problems/left-and-right-sum-differences/description/
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0]
        right = [0]
        for i in range(len(nums) - 1):
            left.append(left[-1] + nums[i])
        for i in range(len(nums) - 1, 0, -1):
            right.append(right[-1] + nums[i])

        right.reverse()
        res = []
        for i in range(len(nums)):
            res.append(abs(left[i] - right[i]))
        return res