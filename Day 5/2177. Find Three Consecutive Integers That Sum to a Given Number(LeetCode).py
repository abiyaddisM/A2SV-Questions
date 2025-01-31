#January 31 2025
#https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        n = num // 3
        return [n - 1, n, n + 1]

