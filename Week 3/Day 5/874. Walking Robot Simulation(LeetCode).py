# February 14 2025
# leetcode.com/problems/walking-robot-simulation/description/?envtype=problem-list-v2&envid=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res = 0
        dicX = {}
        dicY = {}
        for o in obstacles:
            dicX.setdefault(o[0], set()).add(o[1])
            dicY.setdefault(o[1], set()).add(o[0])
        x, y = 0, 0
        rot = 0
        for c in commands:
            if c < 0:
                rot = (rot + (1 if c == -1 else -1)) % 4
            else:
                if rot % 2 == 0:
                    if x not in dicX:
                        y += c if rot == 0 else -c
                        res = max(res, x ** 2 + y ** 2)
                        continue
                else:
                    if y not in dicY:
                        x += c if rot == 1 else -c
                        res = max(res, x ** 2 + y ** 2)
                        continue
                for i in range(c):
                    if rot % 2 == 0:
                        t = (1 if rot == 0 else - 1)
                        if y + t in dicX[x]:
                            break
                        y += t
                    else:
                        t = (1 if rot == 1 else - 1)
                        if x + t in dicY[y]:
                            break
                        x += t
                res = max(res, x ** 2 + y ** 2)

        return res