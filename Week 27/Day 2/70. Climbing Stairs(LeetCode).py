# July 29 2025
# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n: int) -> int:
        self.res = 0
        dic = {}

        def helper(n):
            if n <= 1:
                self.res += 1
                return 1
            if n in dic:
                self.res += dic[n]
                return dic[n]
            temp = helper(n - 1) + helper(n - 2)
            dic[n] = temp
            return temp

        helper(n)
        return self.res