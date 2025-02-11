# February 11 2025
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0
        countDic = {}
        maxs = 0
        sums = 0
        l = 0
        for i in range(len(nums)):
            sums += nums[i]
            countDic[nums[i]] = countDic.get(nums[i],0) + 1
            if i + 1 >= k:
                if len(countDic) == k:
                    maxs = max(maxs,sums)
                countDic[nums[l]] -= 1
                if countDic[nums[l]] == 0:
                    countDic.pop(nums[l])
                sums -= nums[l]
                l += 1

        return maxs