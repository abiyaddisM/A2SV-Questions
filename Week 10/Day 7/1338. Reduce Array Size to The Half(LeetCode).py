# April 6 2025
# https://leetcode.com/problems/reduce-array-size-to-the-half/description/
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        size = len(arr)
        dic = Counter(arr)
        res = 0
        nums = sorted(dic.values(),reverse = True)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total >= size // 2:
                return i + 1
        return res