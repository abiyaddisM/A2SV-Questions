# August 18 2025
# https://leetcode.com/problems/2-keys-keyboard/description/
class Solution:
    def minSteps(self, n: int) -> int:
        temp = [n]
        while n > 1:
            for d in range(n - 1, 0, -1):
                if n % d == 0:
                    temp.append(d)
                    n = d
                    break
        temp.reverse()
        res = 0
        for i in range(len(temp) - 1):
            l = temp[i]
            r = temp[i + 1]
            res += r // l
        return res