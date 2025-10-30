# October 30 2025
# https://leetcode.com/problems/k-items-with-the-maximum-sum/
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = min(numOnes, k)
        k -= res
        k -= numZeros
        res -= min(max(k, 0), numNegOnes)
        return res