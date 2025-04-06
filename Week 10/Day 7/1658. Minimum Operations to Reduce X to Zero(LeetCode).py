# April 6 2025
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        pre = nums[:]
        res = float('inf')
        for i in range(1,len(pre)):
            pre[i] += pre[i - 1]
        nums.append(0)
        total = 0
        for i in range(len(nums)):
            j = -(i + 1)
            total += nums[j]
            t = x - total
            l = 0
            r = len(pre) + j
            if total == x:
                res = min(res,i)
            while l <= r:
                m = (l + r) // 2
                if pre[m] == t:
                    res = min(res,i + m + 1)
                    break
                elif pre[m] > t:
                    r = m - 1
                else:
                    l = m + 1
        if res == float('inf'):
            return -1
        return res