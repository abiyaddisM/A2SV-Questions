# November 9 2025
# https://leetcode.com/problems/relative-sort-array/
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        for i in range(len(arr2)):
            dic[arr2[i]] = i

        temp = []
        for a in arr1:
            if a in dic:
                temp.append((dic[a], a))
                continue
            temp.append((1000 0+ a, a))
        temp.sort()
        res = []
        for t in temp:
            res.append(t[1])
        return res