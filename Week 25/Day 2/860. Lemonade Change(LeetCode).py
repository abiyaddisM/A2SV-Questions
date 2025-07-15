# July 15 2025
# https://leetcode.com/problems/lemonade-change/description/
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5, c10 = 0, 0
        for b in bills:
            if b == 5:
                c5 += 1
            elif b == 10:
                if c5 == 0:
                    return False
                c5 -= 1
                c10 += 1
            elif b == 20:
                if c10 > 0 and c5 > 0:
                    c10 -= 1
                    c5 -= 1
                elif c5 >= 3:
                    c5 -= 3
                else:
                    return False
        return True
