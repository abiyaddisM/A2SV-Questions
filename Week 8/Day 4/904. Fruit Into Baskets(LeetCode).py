# March 20 2025
# https://leetcode.com/problems/fruit-into-baskets/description/
class Solution:
    def totalFruit(self, f: List[int]) -> int:
        res = 0
        dic = {}
        l = 0
        for r in range(len(f)):
            dic[f[r]] = dic.get(f[r],0) + 1
            while len(dic) > 2:
                dic[f[l]] -= 1
                if dic[f[l]] == 0:
                    dic.pop(f[l])
                l += 1
            res = max(res,(r - l) + 1)
        return res