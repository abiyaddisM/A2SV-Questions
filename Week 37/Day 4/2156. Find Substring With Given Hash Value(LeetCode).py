# October 9 2025
# https://leetcode.com/problems/find-substring-with-given-hash-value/description/
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c):
            return ord(c) - 96
        n = len(s)
        p_k = pow(power, k, modulo)
        h = 0
        ans_idx = 0
        for i in range(n - 1, -1, -1):
            h = (h * power + val(s[i])) % modulo
            if i + k < n:
                h = (h - val(s[i + k]) * p_k) % modulo
            if i + k <= n and h == hashValue:
                ans_idx = i
        return s[ans_idx:ans_idx + k]
