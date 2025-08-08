# August 8 2025
# https://leetcode.com/problems/n-th-tribonacci-number/description/
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        arr = [0, 1, 1]
        for i in range(3, n + 1):
            arr.append(arr[-1] + arr[-2] + arr[-3])
        return arr[-1]