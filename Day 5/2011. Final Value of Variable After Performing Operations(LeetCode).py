#January 31 2025
#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for n in operations:
            if n[1] == "+":
                count += 1
            else:
                count -= 1
        return count
