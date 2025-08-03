# August 3 2025
# https://leetcode.com/problems/coin-change/description/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
         dic = {}
         def helper(rem):
            if rem < 0:
                return float('inf')
            if rem == 0:
                return 0
            if rem in dic:
                return dic[rem]
            m = float('inf')
            for c in coins:
                res = helper(rem - c)
                if res != float('inf'):
                    m = min(m, res + 1)
            dic[rem] = m
            return dic[rem]

         res = helper(amount)
         return -1 if res == float('inf') else res
