# November 3 2025
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin = bin(start)[2:]
        goal_bin = bin(goal)[2:]
        res = 0
        for i in range(min(len(start_bin), len(goal_bin))):
            j = -(i + 1)
            if start_bin[j] != goal_bin[j]:
                res += 1
        sg = len(start_bin) > len(goal_bin)
        for i in range(abs(len(goal_bin) - len(start_bin))):
            if sg:
                res += int(start_bin[i])
            else:
                res += int(goal_bin[i])
        return res