# October 9 2025
# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description/?roomId=xHHmDJ
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        if len(a) > n or len(b) > n:
            return []

        def helper(haystack, needle):
            def convert(c):
                return ord(c) - 96

            base = 27
            MOD = 10 ** 9 + 7
            HASH = 0
            resh = 0
            res = [0] * len(haystack)
            for i in range(len(needle)):
                HASH = (HASH * base + convert(needle[i])) % MOD
                resh = (resh * base + convert(haystack[i])) % MOD

            CB = (base ** (len(needle) - 1) % MOD)
            if resh == HASH:
                res[0] = 1
            for i in range(len(needle), len(haystack)):
                old = (convert(haystack[i - len(needle)]) * CB) % MOD
                resh = ((resh - old) * base + convert(haystack[i]) ) % MOD
                if resh == HASH:
                    res[i - len(needle) + 1] = 1
            return res

        newA = helper(s, a)
        newB = helper(s, b)
        pref = [0] * (n + 1)
        # A B C D E F
        for i in range(n):
            if newB[i]:
                left = max(0, i - k)
                right = min(n, i + k + 1)
                pref[left] += 1
                pref[right] += -1

        for i in range(1, n):
            pref[i] += pref[i - 1]
        res = []
        for i in range(n):
            if newA[i] and pref[i] > 0:
                res.append(i)

        return res



