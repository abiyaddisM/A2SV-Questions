# April 12 2025
# https://leetcode.com/problems/can-place-flowers/description/
class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        res = 0
        for i in range(len(f)):
            if f[i] == 1:
                continue
            l = f[i - 1] if i > 0 else 0
            r = f[i + 1] if i < len(f) - 1 else 0
            if l == 0 and r == 0:
                res += 1
                f[i] = 1
        return n <= res