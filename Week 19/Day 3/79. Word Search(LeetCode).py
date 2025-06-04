# June 4 2025
# https://leetcode.com/problems/word-search/description/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def helper(i=0, j=0, index=0):
            if index == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[index]:
                return False
            res = False
            temp = board[i][j]
            board[i][j] = '*'
            res = helper(i + 1, j, index + 1) or res
            res = helper(i - 1, j, index + 1) or res
            res = helper(i, j + 1, index + 1) or res
            res = helper(i, j - 1, index + 1) or res
            board[i][j] = temp
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if helper(i, j):
                    return True
        return False

