# May 4 2025
# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/
class Solution:
    def invert(self, s):
        return ''.join('1' if c == '0' else '0' for c in s)

    def findKthBit(self, n: int, k: int) -> str:
        def helper(n):
            if n == 1:
                return "0"
            res = helper(n - 1)
            res2 = self.invert(res)
            return res + '1' + res2[::-1]

        res = helper(n)
        return res[k - 1]
