# August 23 2025
# https://leetcode.com/problems/last-stone-weight-ii/description/
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dic = {}
        def helper(i, pre):
            if i >= len(stones):
                if pre < 0:
                    return float('inf')
                return pre
            if (i, pre) in dic:
                return dic[(i, pre)]
            t1 = helper(i + 1, stones[i] + pre)
            t2 = helper(i + 1, -stones[i] + pre)
            dic[(i, pre)] = min(t1,t2)
            return min(t1,t2)

        return helper(0, 0)