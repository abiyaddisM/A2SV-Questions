# March 16 2025
# https://leetcode.com/problems/interval-list-intersections/description/
class Solution:
    def intervalIntersection(self, f: List[List[int]], s: List[List[int]]) -> List[List[int]]:
        res = []
        l = 0
        r = 0
        while l < len(f) and r < len(s):
            if s[r][0] <= f[l][1] <= s[r][1] or f[l][0] <= s[r][1]<= f[l][1]:
                p1 = max(s[r][0],f[l][0])
                p2 = min(s[r][1],f[l][1])
                res.append([p1,p2])
            if s[r][1] == f[l][1]:
                l += 1
                r += 1
            elif s[r][1] >= f[l][1]:
                l += 1
            elif s[r][1] <= f[l][1]:
                r += 1
        return res