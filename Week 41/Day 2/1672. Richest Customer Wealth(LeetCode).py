# November 4 2025
# https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for a in accounts:
            res = max(res, sum(a))
        return res