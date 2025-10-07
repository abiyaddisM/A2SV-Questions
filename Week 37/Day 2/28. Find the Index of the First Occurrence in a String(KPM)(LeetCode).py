# October 7 2025
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        if m > n:
            return -1

        pre = [0] * m
        l = 0
        r = 1
        while r < m:
            if needle[l] == needle[r]:
                l += 1
                pre[r] = l
                r += 1
            else:
                if l == 0:
                    r += 1
                else:
                    l = pre[l - 1]

        l = 0
        r = 0
        while r < n:
            if haystack[r] == needle[l]:
                l += 1
                r += 1
                if l == m:
                    return r - l
            else:
                if l != 0:
                    l = pre[l - 1]
                else:
                    r += 1
        return -1
