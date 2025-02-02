#January 31 2025
#https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
class Solution:
    def getLucky(self, st: str, k: int) -> int:
        val = ''
        for s in st:
            val += str(abs(96 - ord(s)))

        for _ in range(k):
            total = 0
            for s in val:
                total += int(s)
            val = str(total)
        return int(val)
