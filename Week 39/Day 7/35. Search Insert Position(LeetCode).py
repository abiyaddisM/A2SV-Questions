# October 26 2025
# https://leetcode.com/problems/search-insert-position/description/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)