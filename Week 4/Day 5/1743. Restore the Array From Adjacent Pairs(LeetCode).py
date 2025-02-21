# February 21 2025
# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/
class Solution:
    def restoreArray(self, ad: List[List[int]]) -> List[int]:
        dic = {}
        res = []
        pre = None
        for a in ad:
            dic[a[0]] = dic.get(a[0], [])
            dic[a[0]].append(a[1])
            dic[a[1]] = dic.get(a[1], [])
            dic[a[1]].append(a[0])
        st = 0
        for k, v in dic.items():
            if len(v) == 1:
                st = k
                break
        while True:
            res.append(st)
            if pre == None or dic[st][0] != pre:
                pre = st
                st = dic[st][0]
            else:
                pre = st
                st = dic[st][1]
            if len(dic[st]) == 1:
                break
        res.append(st)
        return res