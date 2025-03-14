# March 14 2025
# https://leetcode.com/problems/contiguous-array/
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        pre = [-1 if nums[0] == 0 else 1]
        dic = {}
        for i in range(1,len(nums)):
            if nums[i] == 0:
                pre.append(pre[i - 1] - 1)
            else:
                pre.append(pre[i - 1] + 1)
        for i in range(len(pre)):
            arr = dic.get(pre[i],[])
            arr.append(i)
            dic[pre[i]] = arr
        for k, v in dic.items():
            t = 0
            if k == 0:
                t = v[-1] + 1
            else:
                if len(v) > 1:
                    t = v[-1] - v[0]
            res = max(res,t)
        return res