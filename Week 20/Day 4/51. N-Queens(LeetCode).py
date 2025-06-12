# June 12 2025
# https://leetcode.com/problems/n-queens/
import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        check = [['.'] * n for _ in range(n)]
        def isPossible(i, j, check):
            x, y = i, j
            while x > 0 and y > 0:
                x -= 1
                y -= 1
            while x < n and y < n:
                if check[x][y] == 'Q':
                    return False
                x += 1
                y += 1
            x, y = i, j
            while x > 0 and y < n - 1:
                x -= 1
                y += 1
            while x < n and y >= 0:
                if check[x][y] == 'Q':
                    return False
                x += 1
                y -= 1
            for k in range(n):
                if check[k][j] == 'Q' or check[i][k] == 'Q':
                    return False
            return True
        def helper(i, j, check, count):
            if count == n:
                print('d')
                res.append([''.join(c) for c in check])
                return
            if i == n:
                return
            nexti = i + 1 if j == n - 1 else i
            nextj = j + 1 if j != n - 1 else 0
            if isPossible(i, j, check):
                check[i][j] = 'Q'
                helper(i + 1, 0, check, count + 1)
            check[i][j] = '.'
            helper(nexti, nextj, check, count)

        helper(0, 0,check, 0)
        return res