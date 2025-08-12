# August 12 2025
# https://leetcode.com/problems/solving-questions-with-brainpower/description/
class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:

        dic = {}
        def helper(i):
            if i >= len(q):
                return 0
            if i in dic:
                return dic[i]
            include = q[i][0] + helper(i + q[i][1] + 1)
            exclude = helper(i + 1)
            dic[i] = max(include, exclude)
            return dic[i]
        return helper(0)