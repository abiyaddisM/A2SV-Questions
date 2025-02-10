# February 9 2025
# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        myset = set(i for i in range(left,right + 1))
        for r in ranges:
            if r[0] <= right and r[1] >= left:
                s = max(r[0],left)
                e = min(r[1],right)
                for i in range(s,e + 1):
                    myset.discard(i)
        return not myset
