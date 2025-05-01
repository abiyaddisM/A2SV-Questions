# May 1 2025
# https://leetcode.com/problems/count-good-numbers/description/
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        def helper(x,n):
            if n == 0:
                return 1
            if n % 2 == 0:
                t = helper(x, n // 2)
                return (t * t) % MOD
            return (helper(x,n - 1) * x) % MOD


        return helper(5, math.ceil(n / 2)) * helper(4, math.floor(n / 2)) % MOD