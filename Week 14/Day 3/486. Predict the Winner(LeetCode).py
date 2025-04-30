# April 30 2025
# https://leetcode.com/problems/predict-the-winner/description/
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(l, r, i):
            if l == r:
                if i % 2 == 0:
                    return [nums[l], 0]
                return [0, nums[r]]
            t1 = helper(l + 1, r, i + 1)
            t2 = helper(l, r - 1, i + 1)
            if i % 2 == 0:
                if nums[l] + t1[0] >= nums[r] + t2[0]:
                    return [nums[l] + t1[0], t1[1]]
                else:
                    return [nums[r] + t2[0], t2[1]]
            else:
                if nums[l] + t1[1] >= nums[r] + t2[1]:
                    return [t1[0], nums[l] + t1[1]]
                else:
                    return [t2[0], nums[r] + t2[1]]

        temp = helper(0, len(nums) - 1, 0)
        return temp[0] >= temp[1]