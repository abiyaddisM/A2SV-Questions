#February 3 2025
#https://leetcode.com/problems/non-decreasing-array/description/
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modify = False
        l = 0
        for r in range(1, len(nums)):
            if nums[l] > nums[r]:
                if modify: return False
                modify = True
                if l == 0 or nums[l - 1] <= nums[r]:
                    l = r

            else:
                l = r

        return True
