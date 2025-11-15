# November 15 2025
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        active = 0
        for i in range(len(bank)):
            cur = bank[i].count('1')
            if cur > 0:
                res += active * cur
                active = cur
        return res