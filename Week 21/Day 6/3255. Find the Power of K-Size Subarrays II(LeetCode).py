# June 21 2025
# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/description/
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        issue = 0
        res = []
        l = 0
        for r in range(len(nums)):
            pre = nums[r - 1] if r > 0 else nums[r] - 1
            if pre + 1 != nums[r]:
                issue += 1
            if r >= k - 1:
                if issue == 0:
                    res.append(nums[r])
                else:
                    res.append(-1)
                if l != len(nums) - 1 and nums[l] + 1 != nums[l + 1]:
                    issue -= 1
                l += 1

        return res