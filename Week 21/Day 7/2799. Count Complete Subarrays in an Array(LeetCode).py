# June 22 2025
# https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ms = set()
        for n in nums:
            ms.add(n)
        dic = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(nums)):
            dic[nums[r]] += 1
            while len(dic) == len(ms):
                dic[nums[l]] -= 1
                if dic[nums[l]] == 0:
                    dic.pop(nums[l])
                l += 1
            res += l
        return res
