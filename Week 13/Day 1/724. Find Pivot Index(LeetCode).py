# April 21 2025
# https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = nums[:]
        for i in range(1,len(pre)):
            pre[i] += pre[i - 1]
        for i in range(len(pre)):
            left = pre[i - 1] if i > 0 else 0
            right = pre[-1] - pre[i]
            if left == right:
                return i
        return -1