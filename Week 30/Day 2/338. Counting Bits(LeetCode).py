# August 19 2025
# https://leetcode.com/problems/counting-bits/description/
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            res.append(bin(i).count('1'))
        return res