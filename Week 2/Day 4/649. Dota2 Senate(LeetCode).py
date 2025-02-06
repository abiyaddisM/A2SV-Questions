# February 6 2025
# https://leetcode.com/problems/dota2-senate/
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        for i, s in enumerate(senate):
            if s == 'R':
                r.append(i)
            else:
                d.append(i)
        size = len(senate)
        while r and d:
            rpop = r.popleft()
            dpop = d.popleft()
            if dpop > rpop:
                r.append(rpop + size)
            else:
                d.append(dpop + size)



        if r:
            return "Radiant"
        else:
            return "Dire"

