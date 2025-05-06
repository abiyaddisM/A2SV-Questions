# May 6 2025
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left():
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l

        def find_right():
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return r

        if not nums:
            return [-1, -1]

        left = find_left()
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = find_right()
        return [left, right]
