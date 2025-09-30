# September 30 2025
# https://leetcode.com/problems/percentage-of-letter-in-string/description/
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return math.floor(s.count(letter) / len(s) * 100)