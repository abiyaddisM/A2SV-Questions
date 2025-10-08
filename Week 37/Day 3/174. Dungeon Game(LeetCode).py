# October 8 2025
# https://leetcode.com/problems/dungeon-game/description/
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, col = len(dungeon), len(dungeon[0])
        dic = {}
        def dp(i, j):
            if i == row  or j == col:
                return 10**15
            if i == row - 1  and  j == col - 1:
                return max(1, 1 - dungeon[i][j])
            if (i , j) in dic:
                return dic[(i, j)]
            next_need = min(dp(i+1, j), dp(i, j+1))
            dic[(i, j)] =  max(1, next_need - dungeon[i][j])
            return  dic[(i, j)]
        return dp(0, 0)