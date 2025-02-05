# February 4 2025
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/
class Solution:
    def areOccurrencesEqual(self, st: str) -> bool:
        mydic = {}
        for s in st:
            mydic[s] = mydic.get(s,0) + 1
        pre = -1
        for d in mydic:
            if pre != -1 and mydic[d] != pre:
                return False
            pre = mydic[d]
        return True