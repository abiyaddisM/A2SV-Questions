# April 1 2025
# https://leetcode.com/problems/sum-of-square-numbers/description/
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = math.floor(math.sqrt(c))

        while l <= r:
            total = l ** 2 + r ** 2
            if total == c:
                return True
            elif total > c:
                r -= 1
            else:
                l += 1
        return False