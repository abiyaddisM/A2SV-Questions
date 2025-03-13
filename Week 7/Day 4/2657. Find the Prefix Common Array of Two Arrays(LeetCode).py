# March 13 2025
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        dic = {}
        res = []
        count = 0
        for i in range(len(a)):
            dic[a[i]] = dic.get(a[i], 0) + 1
            dic[b[i]] = dic.get(b[i], 0) + 1
            if dic[a[i]] == 2:
                count += 1
            if a[i] != b[i] and dic[b[i]] == 2:
                count += 1
            res.append(count)
        return res