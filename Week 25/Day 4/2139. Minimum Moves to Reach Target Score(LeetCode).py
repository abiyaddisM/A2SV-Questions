# July 15 2025
# https://leetcode.com/problems/minimum-moves-to-reach-target-score/description/
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1:
            if maxDoubles == 0:
                res += target - 1
                break
            if target % 2 == 1:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1
            res += 1
        return res