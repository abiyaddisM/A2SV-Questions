# September 7 2025
# https://leetcode.com/problems/relative-ranks/description/
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort = sorted(score, reverse = True)
        dic = {}
        for i in range(len(sort)):
            if i == 0:
                dic[sort[i]] = 'Gold Medal'
            elif i == 1:
                dic[sort[i]] = 'Silver Medal'
            elif i == 2:
                dic[sort[i]] = 'Bronze Medal'
            else:
                dic[sort[i]] = str(i + 1)
        res = []
        for s in score:
            res.append(dic[s])
        return res