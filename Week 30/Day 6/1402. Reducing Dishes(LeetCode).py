# August 23 2025
# https://leetcode.com/problems/reducing-dishes/description/
class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        sat.sort()
        dic = {}
        def helper(i, index):
            if i >= len(sat):
                return 0
            if (i, index) in dic:
                return dic[(i, index)]
            t1 = helper(i + 1, index + 1) + sat[i] * index
            t2 = helper(i + 1, index)
            dic[(i, index)] = max(t1, t2)
            return dic[(i, index)]

        return helper(0, 1)