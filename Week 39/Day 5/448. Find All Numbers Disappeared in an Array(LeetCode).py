# October 24 2025
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ms = set(nums)
        res = []
        for i in range(len(nums)):
            if i + 1 not in ms:
                res.append(i + 1)
        return res