# June 1 2025
# https://leetcode.com/problems/find-the-substring-with-maximum-cost/description/
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        res = 0
        total = 0
        dic = {}
        for i in range(len(chars)):
            dic[chars[i]] = vals[i]
        l = 0
        for r in range(len(s)):
            if s[r] in dic:
                total += dic[s[r]]\
            else:
                total += ord(s[r]) - 96
            if total < 0:
                total = 0
            res = max(res, total)

        return res