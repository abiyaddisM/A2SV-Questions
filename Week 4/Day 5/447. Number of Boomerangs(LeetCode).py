# February 21 2025
# https://leetcode.com/problems/number-of-boomerangs/description/
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            dic = {}
            for j in range(len(points)):
                if i == j:
                    continue
                total = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                dic[total] = dic.get(total,0) + 1
            for k, v in dic.items():
                res += v * (v - 1)
        return res