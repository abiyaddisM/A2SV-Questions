# July 18 2025
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        last = points[0][1]
        res = 1
        for i in range(1, len(points)):
            if points[i][0] > last:
                res += 1
                last = points[i][1]
                continue
            last = min(last, points[i][1])

        return res