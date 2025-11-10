# November 10 2025
# https://leetcode.com/problems/string-without-aaa-or-bbb/description/
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        ca, cb = a, b

        while ca > 0 or cb > 0:
            la = len(res) >= 2 and res[-1] == 'a' and res[-2] == 'a'
            lb = len(res) >= 2 and res[-1] == 'b' and res[-2] == 'b'

            if la:
                res.append('b')
                cb -= 1
            elif lb:
                res.append('a')
                ca -= 1
            else:
                if ca >= cb and ca > 0:
                    res.append('a')
                    ca -= 1
                elif cb > 0:
                    res.append('b')
                    cb -= 1

        return "".join(res)
