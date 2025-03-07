# March 7 2025
# https://leetcode.com/problems/find-right-interval/description/

class Solution:
    def findRightInterval(self, iv: List[List[int]]) -> List[int]:
        def helper(a):
            l = 0
            r = len(iv) - 1
            while r >= l:
                m = (l + r) // 2
                if iv[m][0] == a:
                    return m
                elif iv[m][0] > a:
                    r = m - 1
                else:
                    l = m + 1
            if l < len(iv):
                return l
            return -1

        dic = {}
        for i in range(len(iv)):
            dic[iv[i][0]] = i
        iv2 = iv[:]
        iv.sort(key = lambda x : x[0])
        res = []
        for i in range(len(iv)):
            temp = helper(iv2[i][1])
            if temp == -1:
                res.append(-1)
            else:
                res.append(dic[iv[temp][0]])
        return res