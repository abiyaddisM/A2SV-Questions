# June 26 2025
# https://leetcode.com/problems/evaluate-division/description/
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = defaultdict(dict)
        for i in range(len(equations)):
            dic[equations[i][0]][equations[i][1]] = values[i]
            dic[equations[i][1]][equations[i][0]] = 1/values[i]

        def helper(sor, des, visited):
            if sor not in dic or des not in dic:
                return -1

            if sor == des:
                return 1
            visited.add(sor)
            for k, v in dic[sor].items():
                if k in visited:
                    continue
                temp = helper(k, des, visited)
                if temp != -1:
                    return temp * v
            return -1

        res = []
        for q in queries:
            if not q[0] in dic or not q[1] in dic:
                if q[0] == q[1]:
                    res.append(-1)
                    continue
            if q[0] == q[1]:
                res.append(1)
                continue
            visited = set()
            res.append(helper(q[0], q[1], visited))
        return res