# February 4 2025
# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        mydic = {}
        res = []
        for n in nums:
            mydic[n] = mydic.get(n,0) + 1
            if mydic[n] > 1:
                res.append(n)
        return res