# May 19 2025
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)
        for i in range(small,-1,-1):
            if large % i == 0 and small % i == 0:
                return i