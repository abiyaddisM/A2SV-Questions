# March 4 2025
# https://leetcode.com/problems/image-overlap/description/
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        r1 = [(i,j) for i in range(len(img1)) for j in range(len(img1)) if img1[i][j]]
        r2 = [(i,j) for i in range(len(img2)) for j in range(len(img2)) if img2[i][j]]
        dic = {}
        for a, b in r1:
            for c, d in r2:
                out = (a - c, b - d)
                dic[out] = dic.get(out,0) + 1
        return max(dic.values() or [0])