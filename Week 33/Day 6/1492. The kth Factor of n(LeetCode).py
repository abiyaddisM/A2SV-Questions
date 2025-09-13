# September 13 2025
# https://leetcode.com/problems/the-kth-factor-of-n/description/
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        for i in range(1, n + 1):
            if n % i == 0:
                res.append(i)
        if len(res) < k:
            return -1
        return res[k -1]
    