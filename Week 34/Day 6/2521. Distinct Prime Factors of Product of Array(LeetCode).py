# September 20 2025
# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/description/
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()

        def helper(x):

            if x % 2 == 0:
                res.add(2)
                while x % 2 == 0:
                    x //= 2
            temp = 3
            while temp * temp <= x:
                if x % temp == 0:
                    res.add(temp)
                    while x % temp == 0:
                        x //= temp
                temp += 2
            if x > 1:
                res.add(x)

        for n in nums:
            helper(n)
        return len(res)