# October 8 2025
# https://leetcode.com/problems/repeated-string-match/description/
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if len(a) >= len(b):
            if b in a:
                return 1
            if b in a + a:
                return 2
            return -1

        l, r = 0, 1
        LPS = [0 for _ in range(len(b))]
        while r < len(b):
            if b[l] == b[r]:
                l += 1
                LPS[r] = l
                r += 1
            else:
                if l == 0:
                    LPS[r] = 0
                    r += 1
                else:
                    l = LPS[l - 1]
        n, m = len(a), len(b)
        l = 0
        for i in range(m + n):
            ch = a[i % n]
            while l > 0 and ch != b[l]:
                l = LPS[l - 1]
            if ch == b[l]:
                l += 1
                if l == m:
                    return (i + 1 + n - 1) // n

        return -1
