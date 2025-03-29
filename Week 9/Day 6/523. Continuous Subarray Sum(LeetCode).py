# March 29 2025
# https://leetcode.com/problems/continuous-subarray-sum/
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {}
        total = nums[0]
        dic[total % k] = 0
        for i in range(1, len(nums)):
            total += nums[i]
            temp = total % k
            if temp == 0:
                return True
            if temp in dic:
                if dic[temp] != i - 1:
                    return True
            else:
                dic[temp] = i

        return False