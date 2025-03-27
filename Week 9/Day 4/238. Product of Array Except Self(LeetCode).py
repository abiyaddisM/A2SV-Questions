# March 27 2025
# https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suf = [1]
        pre = [1]
        for i in range(len(nums)):
            j = -(i + 1)
            pre.append(pre[-1] * nums[i])
            suf.append(suf[-1] * nums[j])
        suf.pop()
        pre.pop()
        suf.reverse()
        for i in range(len(pre)):
            pre[i] *= suf[i]
        return pre