# March 18 2025
# https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, house: List[int], heat: List[int]) -> int:
        house.sort()
        heat.sort()
        res = 0
        for h in house:
            l = 0
            r = len(heat) - 1
            while l <= r:
                m = (l + r) // 2
                if heat[m] == h:
                    break
                elif heat[m] > h:
                    r = m - 1
                else:
                    l = m + 1
            m = 0
            if l <= r:
                m = (l + r) // 2
            else:
                if l >= len(heat):
                    m = r
                elif r < 0:
                    m = l
                else:
                    if abs(h - heat[l]) < abs(h - heat[r]):
                        m = l
                    else:
                        m = r
            res = max(abs(heat[m] - h), res)
        return res
