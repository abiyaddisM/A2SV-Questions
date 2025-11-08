# November 8 2025
# https://leetcode.com/problems/greatest-common-divisor-of-strings/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        g = gcd(len(str1), len(str2))

        return str1[:g]
