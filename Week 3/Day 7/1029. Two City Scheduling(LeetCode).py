# February 16 2025
# https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[1] - x[0],reverse = True)
        res = 0
        for i in range(len(costs)):
            if i < len(costs) // 2:
                res += costs[i][0]
            else:
                res += costs[i][1]

        return res