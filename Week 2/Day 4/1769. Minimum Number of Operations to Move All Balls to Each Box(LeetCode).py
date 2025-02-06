# February 6 2025
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        one = [i for i in range(len(boxes)) if boxes[i] == '1']
        res = []
        for i in range(len(boxes)):
            total = 0
            for j in range(len(one)):
                total += abs(i - one[j])
            res.append(total)
        return res