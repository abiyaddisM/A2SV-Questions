# September 15 2025
# https://leetcode.com/problems/delete-columns-to-make-sorted/description/
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for i in range(len(strs[0])):
            temp = []
            for j in range(len(strs)):
                temp.append(strs[j][i])
            t = ''.join(sorted(temp))
            temp = ''.join(temp)
            if t != temp:
                res += 1
        return res