# April 24 2025
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = deque()
        minq = deque()
        res = 0
        l = 0
        for r in range(len(nums)):
            while maxq and maxq[-1] < nums[r]:
                maxq.pop()
            while minq and minq[-1] > nums[r]:
                minq.pop()
            maxq.append(nums[r])
            minq.append(nums[r])
            while maxq and minq and maxq[0] - minq[0] > limit:
                if nums[l] == maxq[0]:
                    maxq.popleft()
                if nums[l] == minq[0]:
                    minq.popleft()
                l += 1

            res = max(res,r - l + 1)
        return res