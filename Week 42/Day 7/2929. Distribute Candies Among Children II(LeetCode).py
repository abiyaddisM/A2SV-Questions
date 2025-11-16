# November 16 2025
# https://leetcode.com/problems/distribute-candies-among-children-ii/description/
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def ways(t: int) -> int:
            if t < 0:
                return 0
            k = t + 2
            return k * (k - 1) // 2

        L = limit + 1

        ans = 0
        ans += ways(n)
        ans -= 3 * ways(n - L)
        ans += 3 * ways(n - 2 * L)
        ans -= ways(n - 3 * L)

        return ans
