# April 7 2025
# https://leetcode.com/problems/count-number-of-nice-subarrays/
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        dic = Counter(nums)
        dic[0] += 1
        print(dic)
        for key, v in dic.items():
            if key - k in dic:
                res += v * dic[key - k]
        return res

