# April 13 2025
# https://leetcode.com/problems/k-closest-points-to-origin/description/

class Solution:
    def kClosest(self, p: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        for i in range(len(p)):
            cal = (p[i][0] ** 2) + (p[i][1] ** 2)
            temp.append([cal, i])
        temp.sort(key = lambda x : x[0])
        res = []
        for i in range(k):
            res.append(p[temp[i][1]])
        return res