# March 10 2025
#https://leetcode.com/problems/longest-square-streak-in-an-array/?envType=problem-list-v2&envId=sorting
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        ms = set(nums)
        res = 0
        for n in nums:
            c = 0
            temp = n
            while temp ** 2 in ms:
                temp **= 2
                ms.discard(temp)
                c += 1
            res = max(res, c)
        return res + 1 if res > 0 else -1