# November 18 2025
# https://leetcode.com/problems/check-if-it-is-a-good-array/description/?envType=problem-list-v2&envId=number-theory
class Solution:
    def isGoodArray(self, nums):
        overall_gcd = reduce(gcd, nums)
        return overall_gcd == 1