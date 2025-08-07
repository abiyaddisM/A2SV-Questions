# August 7 2025
# https://leetcode.com/problems/pascals-triangle-ii/description/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1,rowIndex  + 1):
            temp = [1]
            for j in range(len(res) -1):
                temp.append(res[j] + res[j + 1])
            temp.append(1)
            res = temp
        return res
