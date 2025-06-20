# June 20 2025
# https://leetcode.com/problems/number-of-provinces/
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = [ False for __ in range(len(isConnected))]
        def helper(row):
            visited[row] = True
            for j in range(len(isConnected)):
                if not visited[j] and isConnected[row][j] == 1:
                    helper(j)

        for i in range(len(isConnected)):
            if not visited[i]:
                res += 1
                helper(i)
        return res

