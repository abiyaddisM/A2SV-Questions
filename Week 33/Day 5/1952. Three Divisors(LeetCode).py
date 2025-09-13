# September 12 2025
# https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory
class Solution:
    def isThree(self, n: int) -> bool:
        res = 0
        for i in range(n, 0, -1):
            if n % i == 0:
                res += 1
        return res == 3