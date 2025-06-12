# June 12 2025
# https://leetcode.com/problems/find-the-town-judge/description/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        dic1 = defaultdict(list)
        dic2 = defaultdict(list)
        for t in trust:
            dic1[t[1]].append(t[0])
        for t in trust:
            dic2[t[0]].append(t[1])
        for k, v in dic1.items():
            if len(v) == n - 1 and k not in dic2:
                return k
        return -1