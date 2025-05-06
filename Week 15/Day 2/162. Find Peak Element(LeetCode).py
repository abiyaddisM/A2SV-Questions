# May 6 2025
# https://leetcode.com/problems/find-peak-element/description/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            l = nums[mid - 1] if mid > 0 else float('-inf')
            r = nums[mid + 1] if mid < n - 1 else float('-inf')

            if l < nums[mid] and r < nums[mid]:
                return mid
            elif r > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1