# February 6 2025
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mydic = {}
        for i in range(len(list1)):
            if list1[i] not in mydic:
                mydic[list1[i]] = i
        res = []
        mins = 2000
        for i in range(len(list2)):
            if list2[i] in mydic:
                size = i + mydic[list2[i]]
                if size < mins:
                    mins = size
                    res = [list2[i]]
                elif size == mins:
                    res.append(list2[i])
        return res



