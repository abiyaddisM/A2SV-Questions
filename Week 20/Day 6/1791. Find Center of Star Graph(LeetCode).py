# June 14 2025
# https://leetcode.com/problems/find-center-of-star-graph/description/
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = {}
        for i in range(len(edges)):
            dic[edges[i][0]] = dic.get(edges[i][0], 0) + 1
            dic[edges[i][1]] = dic.get(edges[i][1], 0) + 1
        return max(dic, key = dic.get)