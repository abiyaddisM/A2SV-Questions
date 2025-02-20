# February 20 2025
# https://leetcode.com/problems/image-smoother/description/
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(img)):
            res.append([])
            for j in range(len(img[i])):
                t = 0
                c = 0
                for k in range(i - 1,i + 2):
                    for l in range(j - 1,j + 2):
                        if k >= 0 and k < len(img) and l >= 0 and l < len(img[i]):
                            t += img[k][l]
                            c += 1
                res[i].append(t//c)
        return res
