# April 26 2025
# https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
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
            while maxq[0] - minq[0] > 2:
                if maxq[0] == nums[l]:
                    maxq.popleft()
                if minq[0] == nums[l]:
                    minq.popleft()
                l += 1
            res += r - l + 1
        return res
