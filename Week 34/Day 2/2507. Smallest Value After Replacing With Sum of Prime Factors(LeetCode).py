# September 16 2025
# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/description/
class Solution:
    def smallestValue(self, n: int) -> int:
        def dofactor(n):
            orig = n
            factors = []
            while n % 2 == 0:
                factors.append(2)
                n //= 2

            i = 3
            while i * i <= n:
                while n % i == 0:
                    factors.append(i)
                    n //= i
                i += 2

            if n > 2:
                factors.append(n)

            if len(factors) != 1:
                s = sum(factors)
                if s == orig:
                    return s
                return dofactor(s)
            return factors[0]

        return dofactor(n)
