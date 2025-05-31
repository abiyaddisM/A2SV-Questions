# May 31 2025
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/
class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        i = 0
        while i < len(s):
            if s[i:i + 3][-1] == '#':
                temp = s[i:i + 2]
                res += chr(96 + int(temp))
                i += 3
            else:
                res += chr(96 + int(s[i]))
                i += 1
        return res