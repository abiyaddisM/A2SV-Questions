# August 31 2025
# https://leetcode.com/problems/long-pressed-name/description/
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def helper(x):
            x += '*'
            res = []
            l = 0
            for r in range(len(x) - 1):
                if x[r] != x[r + 1]:
                    res.append(x[l: r + 1])
                    l = r + 1
            return res
        t1 = helper(name)
        t2 = helper(typed)
        if len(t1) != len(t2):
            return False
        for i in range(len(t1)):
            if t1[i][0] != t2[i][0] or len(t2[i]) < len(t1[i]):
                return False
        return True
