# August 6 2025
# https://leetcode.com/problems/decode-ways/description/
class Solution:
    def numDecodings(self, s: str) -> int:
        dic = {}

        def helper(i):
            if i >= len(s):
                return 1
            l = s[i:i + 1]
            r = s[i:i + 2]
            if l == '0':
                return 0
            if i in dic:
                return dic[i]
            include = 0
            if '1' <= r <= '26' and len(r) == 2:
                include = helper(i + 2)
            exclude = helper(i + 1)
            dic[i] = include + exclude
            return dic[i]

        return helper(-1)