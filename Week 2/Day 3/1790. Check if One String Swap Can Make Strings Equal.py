# February 5 2025
#https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        size = len(s1)
        count = 0
        dic1 = Counter(s1)
        dic2 = Counter(s2)
        for d in dic1:
            if d not in dic2:
                return False
            if dic1[d] != dic2[d]:
                return False
        for i in range(size):
            if s1[i] != s2[i]:
                count += 1
            if count == 3:
                return False
        return True