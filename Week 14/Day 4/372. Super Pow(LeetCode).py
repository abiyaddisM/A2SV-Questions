# May 1 2025
# https://leetcode.com/problems/super-pow/description/
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        temp = 0
        for n in b:
            temp = (temp * 10 + n) % 1140
        if temp == 0:
            temp = 1140
        return ((a % MOD) ** temp) % MOD
