# February 4 2025
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mydic = {}
        res = [[],[]]
        for m in matches:
            if m[0] not in mydic:
                mydic[m[0]] = 0
            mydic[m[1]] = mydic.get(m[1],0) + 1
        for d in mydic:
            if mydic[d] == 0:
                res[0].append(d)
            elif mydic[d] == 1:
                res[1].append(d)
        res[0].sort()
        res[1].sort()
        return res